def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strings must be equal")

    count = 0

    for a, b in zip(strand_a, strand_b):
        if a != b:
            count += 1
    
    return count
