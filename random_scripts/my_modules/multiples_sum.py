def multiples_3_5_sum(limit):
    """This function will sum the multiples of 3 & 5"""
    m_3 = []
    m_5 = []
    for i in range(limit):
        if i % 3 == 0:
            m_3.append(i)
        elif i % 5 == 0:
            m_5.append(i)
        else:
            pass

    sum_all = sum(m_3 + m_5)
    print(f'Sum of all natural numbers between {limit} which are multiples of 3 & 5 is {sum_all}')


if __name__ == "__main__":
    print('Printing the default sum of natural numbers. Multiples of 3 & 5 only.')
    multiples_3_5_sum(10)



