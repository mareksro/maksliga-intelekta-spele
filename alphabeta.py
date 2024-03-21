def is_terminal(node):
  # Spele beidzas kad akmenu vairs nav
  return node.akmeni == 0

def static_evaluation(node):
  # Spēlētāja iegūto akmeņu skaits tiek pievienots spēlētāja rezultātam.
  # Ja pēc akmeņu ņemšanas uz galda ir palicis pāra skaits akmeņu,
  # tad spēlētāja rezultātam tiek pievienoti 2 punkti, un, ja ir nepāra skaitlis,
  # tad tiek atskaitīti 2 punkti.
  if node.akmeni % 2 == 0:
      node.speletaja_punkti += 2
  else:
      node.speletaja_punkti -= 2

  node.speletaja_punkti += node.stones_taken

  # Ja spēlētājiem ir vienāds punktu skaits, rezultāts ir neizšķirts.
  # Pretējā gadījumā uzvar spēlētājs, kuram ir vairāk punktu.
  if node.speletaja_punkti == node.pretinieka_punkti:
      return 0  # Neizskirts
  elif node.speletaja_punkti > node.pretinieka_punkti:
      return 1  # Speletajs uzvar
  else:
      return -1  # Dators uzvar

def minimax(node, depth, alpha, beta, maximizingPlayer):
  if depth == 0 or is_terminal(node):
      return static_evaluation(node)

  if maximizingPlayer:
      maxEva = float('-inf')
      for child in node.children():
          eva = minimax(child, depth-1, alpha, beta, False)
          maxEva = max(maxEva, eva)
          alpha = max(alpha, eva)
          if beta <= alpha:
              break
      return maxEva

  else:
      minEva = float('inf')
      for child in node.children():
          eva = minimax(child, depth-1, alpha, beta, True)
          minEva = min(minEva, eva)
          beta = min(beta, eva)
          if beta <= alpha:
              break
      return minEva
