female(jaya).
female(vinni).

male(venkat).
male(subhash).

parent(jaya,vinni).
parent(jaya,subhash).
parent(venkat,vinni).
parent(venkat,subhash).
parent(vinni,subhash).
parent(subhash,vinni).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
sister(X,Y):-parent(X,Y),female(X).
brother(X,Y):-parent(X,Y),male(X).
