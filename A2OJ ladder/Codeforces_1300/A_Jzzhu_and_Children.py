num_children , num_candies = [int(x) for x in input().split(" ")]
children = [int(x) for x in input().split(" ")]

children_order = [i for i in range(num_children)]

last_child = children_order[-1]

while len(children_order) > 0:
    last_child = children_order[-1]
    # print(children_order)
    # print(children)
    child = 0
    if num_candies < children[child]:
        # print(f"Child {child+1} wants {children[child]} candies but only gets {num_candies} candies")
        children_order.append(children_order[child])
        children_order.pop(child)
        children[child] -= num_candies
        children.append(children[child])
        children.pop(child)
        last_child = child
        child -= 1
    else:
        # print(f"Child {child+1} wants {children[child]} candies and gets {num_candies} candies")
        # print(child)
        # print(children_order[child])
        children.pop(child)
        children_order.pop(child)
        child -= 1
    child += 1
    

    
print(last_child+1)