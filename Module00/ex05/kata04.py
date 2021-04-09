t = ( 0, 4, 132.42222, 10000, 12345.67)

print('day_{day}, ex_{ex} : {n1}, {n2:.2e}, {n3:.2e}'.format(day=str(t[0]).zfill(2),ex=str(t[1]).zfill(2),n1=round(t[2],2),n2=t[3],n3=t[4]))