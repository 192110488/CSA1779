

on(monkey,floor).
on(chair,floor).
in(monkey,room).
in(chair,room).
in(banana,room).
at(banana,ceiling).

strong(monkey).
grasp(monkey).
climb(monkey,chair).

push(monkey,chair):-
    strong(monkey).

under(banana,chair):-
    push(monkey,chair).


canreach(monkey,banana):-
    at(banana,floor),
    at(banana,ceiling),
    under(banana,chair),
    climb(monkey,chair).

canget(monkey,banana):-
    canreach(monkey,banana),grasp(monkey).
