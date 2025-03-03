# Vytvoření instance Facebooku
from collections import deque


class User():
    def __init__(self, name) -> None:
        self._name = name
        self._friends: list[str] = []

class Facebook():
    def __init__(self) -> None:
        self._userlist: dict[str, User] = {}

    def pridej_uzivatel(self, name) -> None:
        self._userlist[name] = User(name)
    
    def pridej_znamost(self, name1, name2) -> None:
        user1 = self._userlist[name1]
        user2 = self._userlist[name2]

        if name2 not in user1._friends:
            user1._friends.append(name2)

        if name1 not in user2._friends:
            user2._friends.append(name1)

    def jak_daleko(self, name1, name2) -> str | None:
        fronta = deque()
        fronta.append((name1, 1))
        done = set(name1)

        while fronta:
            current_user, dist = fronta.popleft()

            for friend in self._userlist[current_user]._friends:
                if friend == name2:
                    return dist
            
            if friend not in done:
                done.add(friend)
                fronta.append((friend, dist + 1))

        return None






fb = Facebook()

# Seznam unikátních jmen
jmena = [
    "Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
    "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
    "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"
]

# Vkládání známostí do Facebooku
for jmeno in jmena:
    fb.pridej_uzivatel(jmeno)
  
# Hardkodované známosti
znamosti = [
    ("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"),
    ("Cyril", "Emil"), ("Cyril", "František"), ("Dana", "Gabriela"),
    ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"),
    ("Hana", "Karel"), ("Ivan", "Lenka"), ("Jana", "Marek"),
    ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
    ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"),
    ("Quentin", "Tereza"), ("Radka", "Urbán"), ("Stanislav", "Veronika"),
    ("Tereza", "Walter"), ("Urbán", "Xenie"), ("Veronika", "Yvona"),
    ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
    ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")
]

# Vkládání známostí do Facebooku
for clovek1, clovek2 in znamosti:
    fb.pridej_znamost(clovek1, clovek2)

print(fb.jak_daleko("Lenka", "Radka"))