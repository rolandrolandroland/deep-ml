def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              if len(a[0]) != len(b):
                out = -1
              else:
                    out = []
                    for i in range(len(a)):
                        result_row = []
                        for j in range(len(b[0])):
                            row = a[i]
                            col = [row[j] for row in b]
                            val = sum(x * y for x,y in zip(row, col))
                            result_row.append(val)
                        out.append(result_row)


              return out