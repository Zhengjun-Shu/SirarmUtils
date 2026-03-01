def getBatch(size, *args):
    """
    Batch generator that groups multiple iterables into chunks of specified size.| 批量生成器，将多个可迭代对象按指定大小分组。

    Args:
        size (int): The batch size for grouping elements. | 分组元素的批次大小。
        *args: Variable length argument list of iterables to be batched. | 可变长度参数列表，包含需要批处理的可迭代对象。

    Yields:
        tuple: A tuple containing lists of elements from each input iterable, grouped by the specified batch size.| 包含来自每个输入可迭代对象的元素列表的元组，按指定的批次大小进行分组。

    Example:
        >>> a = [1, 2, 3, 4, 5]
        >>> b = ['a', 'b', 'c', 'd']
        >>> for batch_a, batch_b in getBatch(2, a, b):
        ...     print(batch_a, batch_b)
        [1, 2] ['a', 'b']
        [3, 4] ['c', 'd']
        [5] []
    """
    import itertools

    l = len(args)
    list_object = {}
    cur_batch = 0
    for items in itertools.zip_longest(*args, fillvalue=None):
        for i in range(l):
            if items[i] is not None:
                list_object.setdefault(i, []).append(items[i])
        cur_batch += 1
        if cur_batch >= size:
            yield [list_object.get(j, []) for j in range(l)]
            list_object = {}
            cur_batch = 0
    if any(list_object.get(j, []) for j in range(l)):
        yield [list_object.get(j, []) for j in range(l)]


if __name__ == "__main__":
    a = [1, ]
    b = [11, 12, 13]
    for batch_a, batch_b in getBatch(2, a, b):
        print(batch_a, batch_b)
