def evaluate(pred_joins, gt_joins):
    """ Evaluate the performance of fuzzy joins

    Parameters
    ----------
    pred_joins: list
        A list of tuple pairs (id_l, id_r) that are predicted to be matches

    gt_joins:
        The ground truth matches

    Returns
    -------
    precision: float
        Precision score

    recall: float
        Recall score

    f1: float
        F1 score
    """
    pred = {(l, r) for l, r in pred_joins}
    gt = {(l, r) for l, r in gt_joins}
    tp = pred.intersection(gt)

    precision = len(tp) / len(pred)
    recall = len(tp) / len(gt)
    f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1
