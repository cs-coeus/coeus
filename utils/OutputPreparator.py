import copy

from models.ModelClustering import ModelClustering
from models.ModelGensim import ModelGensim


class OutputPreparator:

    def __init__(self):
        OutputPreparator.THRESHOLD = 0.4
        OutputPreparator.clustering_model = ModelClustering()

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
                    if text1 == text2 or ModelGensim.get_similarity_two_word_by_w2v(
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
    def topic_clustering_for_unstructured_result(json_output):
        child_node_id_of_root = OutputPreparator._get_child_node_id_of_root(json_output)
        level_1_nodes = OutputPreparator._get_text_from_ids_array(child_node_id_of_root, json_output)
        X_input, nodes_map_to_X = OutputPreparator._generate_X_for_k_medoids_clustering(level_1_nodes)
        best_k, best_cluster, center = OutputPreparator.clustering_model.k_medoids_clustering(X_input)
        if best_k == -1:
            return json_output
        nodes_with_embbeding_map_with_cluster = OutputPreparator._find_center_node_and_label(best_cluster, center,
                                                                                             nodes_map_to_X)
        new_json_output = OutputPreparator._build_new_json_from_clustering(best_cluster, center,
                                                                           nodes_with_embbeding_map_with_cluster,
                                                                           json_output)
        return new_json_output

    @staticmethod
    def _get_child_node_id_of_root(json_output):
        target_node = []
        for edge in json_output['edges']:
            if edge['parentId'] == 1:
                target_node += [edge['childId']]
        return target_node

    @staticmethod
    def _get_text_from_ids_array(array_of_ids, json_output):
        nodes = []
        for node in json_output['nodes']:
            if node['id'] in array_of_ids:
                nodes += [node]
        return nodes

    @staticmethod
    def _generate_X_for_k_medoids_clustering(array_of_nodes):
        X = []
        node_ids_map_to_X = []
        for i, node in enumerate(array_of_nodes):
            word_embedded = ModelGensim.get_word_embedded(node['text'])
            if type(word_embedded) == type('str'):
                continue
            else:
                X += [word_embedded]
                node_ids_map_to_X += [{'id': node['id'], 'text': node['text'], 'embedded': word_embedded}]
        return X, node_ids_map_to_X

    @staticmethod
    def _find_center_node_and_label(_cluster_label, _centers, _nodes_with_embbeding):
        _nodes_with_embbeding_copy = copy.deepcopy(_nodes_with_embbeding)
        for i, label in enumerate(_cluster_label):
            _nodes_with_embbeding_copy[i]['label'] = label

        for center in _centers:
            for node in _nodes_with_embbeding_copy:
                if str(node['embedded']) == str(center):
                    node['center'] = True
        for node in _nodes_with_embbeding_copy:
            del node['embedded']
        return _nodes_with_embbeding_copy

    @staticmethod
    def _build_new_json_from_clustering(_best_cluster, _center, _nodes_with_embbeding_map_with_cluster, _original_json):
        _original_json_copy = copy.deepcopy(_original_json)
        new_parent_map = {}
        nodes_id_label_map = {}
        for node in _nodes_with_embbeding_map_with_cluster:
            keys = node.keys()
            nodes_id_label_map[node['id']] = node['label']
            if 'center' in keys and node['center']:
                new_parent_map[node['label']] = node['id']

        list_of_node_to_be_update = nodes_id_label_map.keys()
        for edge in _original_json_copy['edges']:
            if edge['childId'] in list_of_node_to_be_update:
                if edge['childId'] == new_parent_map[nodes_id_label_map[edge['childId']]]:
                    edge['parentId'] = 1
                else:
                    edge['parentId'] = new_parent_map[nodes_id_label_map[edge['childId']]]
        return _original_json_copy

    @staticmethod
    def post_processing(algorithm_output_final_json, is_semi_structure):
        pruned_output = OutputPreparator.pruning(algorithm_output_final_json)
        if is_semi_structure:
            return pruned_output
        return OutputPreparator.topic_clustering_for_unstructured_result(pruned_output)