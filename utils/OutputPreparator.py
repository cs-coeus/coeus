import copy
import spacy
import torch


class OutputPreparator:

    def __init__(self):
        OutputPreparator.THRESHOLD = 0.6
        if torch.cuda.is_available():
            spacy.require_gpu()
        OutputPreparator.nlp = spacy.load('en_core_web_lg')

    @staticmethod
    def pruning(algorithm_output_final_json):
        nodes = copy.deepcopy(algorithm_output_final_json['nodes'])
        edges = copy.deepcopy(algorithm_output_final_json['edges'])

        grouped_edges = OutputPreparator._group_concepts_with_same_parent(
            edges)
        grouped_edges = OutputPreparator._remove_non_data_concepts(
            grouped_edges)
        grouped_edges = OutputPreparator._remove_empty_set(grouped_edges)

        for group in grouped_edges:
            members_with_parent = [group, *grouped_edges[group]]
            to_be_delete_id_set = set()
            for i in range(len(members_with_parent)):
                for j in range(i + 1, len(members_with_parent)):
                    id1 = members_with_parent[i]
                    id2 = members_with_parent[j]
                    if id1 in to_be_delete_id_set or id2 in to_be_delete_id_set:
                        continue
                    text1 = OutputPreparator._get_node_by_id(id1, nodes)[
                        'text'].lower()
                    text2 = OutputPreparator._get_node_by_id(id2, nodes)[
                        'text'].lower()
                    if text1 == text2 or OutputPreparator.check_similarity_two_word(
                            text1, text2) > OutputPreparator.THRESHOLD:
                        if id1 in grouped_edges.keys():
                            to_be_delete_id_set.add(id2)
                            break
                        if id2 in grouped_edges.keys():
                            to_be_delete_id_set.add(id1)
                            break
                        if id1 < id2:
                            to_be_delete_id_set.add(id2)
                        else:
                            to_be_delete_id_set.add(id1)

            if len(to_be_delete_id_set) > 0:
                copied_current_group = copy.deepcopy(grouped_edges[group])
                for id in to_be_delete_id_set:
                    copied_current_group.remove(id)

                    remove_node = OutputPreparator._get_node_by_id(id, nodes)
                    nodes.remove(remove_node)

                    remove_edges = [
                        edge for edge in edges if edge['childId'] == id]
                    for remove_edge in remove_edges:
                        edges.remove(remove_edge)
                grouped_edges[group] = copied_current_group

        number_of_removed_nodes = len(
            algorithm_output_final_json["nodes"]) - len(nodes)
        percentage_of_removed_nodes = round(
            (number_of_removed_nodes / len(algorithm_output_final_json["nodes"])) * 100, 2)
        print(
            f'Removed {number_of_removed_nodes} nodes. ({percentage_of_removed_nodes}%)')

        return {'nodes': nodes, 'edges': edges}

    @staticmethod
    def _get_node_by_id(id, nodes):
        id_list = [node['id'] for node in nodes]
        idx = id_list.index(id)
        return nodes[idx]

    @staticmethod
    def check_similarity_two_word(word1, word2):
        tokens = OutputPreparator.nlp(word1 + ' ' + word2)
        token1, token2 = tokens[0], tokens[1]
        return token1.similarity(token2)

    @staticmethod
    def _remove_empty_set(grouped_edges):
        copied_grouped_edges = grouped_edges.copy()
        for group in grouped_edges:
            if len(grouped_edges[group]) == 0:
                copied_grouped_edges.pop(group, None)
        return copied_grouped_edges

    @staticmethod
    def _group_concepts_with_same_parent(edges):
        grouped_edges = dict()
        for edge in edges:
            parent_id = edge['parentId']
            child_id = edge['childId']

            if parent_id in grouped_edges:
                grouped_edges[parent_id].add(child_id)
            else:
                grouped_edges[parent_id] = {child_id}
        return grouped_edges

    @staticmethod
    def _remove_non_data_concepts(grouped_edges):
        copied_grouped_edges = grouped_edges.copy()
        for group in copied_grouped_edges:
            current_group = copied_grouped_edges[group]
            copied_current_group = current_group.copy()
            for member in current_group:
                if member in copied_grouped_edges:
                    copied_current_group.remove(member)
            copied_grouped_edges[group] = copied_current_group
        return copied_grouped_edges

    @staticmethod
    def post_processing(algorithm_output_final_json):
        pruned_output = OutputPreparator.pruning(algorithm_output_final_json)
        return pruned_output
