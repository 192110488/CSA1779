bird(sparrow).
bird(pegion).
bird(parrot).
bird(peacock).
bird(hen).

can_fly(X):-bird(X).
can_fly(pegion):-false.
