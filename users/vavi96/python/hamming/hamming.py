def distance(strand_a, strand_b):

  if len(strand_a)!=len(strand_b): 
    raise ValueError('Not match')
  count=0
  for index in range(len(strand_a)):
     if strand_a[index]!=strand_b[index]: 
         # pos1,pos2 indexes in   strand_a,strand_b
       count=count + 1
  return count
