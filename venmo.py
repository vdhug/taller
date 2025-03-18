class User:
    def __init__(self, name: str, balance: float = 0):
        self.name = name
        self.balance = balance
        self.credit = 0
        self.friends = []
        self.activities = []


    def pay(self, user, quantity: float, reason: str):
        if quantity <= 0:
            raise Exception("Declined")
        try:
            if self.balance >= quantity:
                self.balance = self.balance - quantity
                self.activities.append(f"{self.name} paid ${quantity} to {user.name} for {reason} (BALANCE)")
            else:
                self.credit = self.credit - quantity
                self.activities.append(f"{self.name} paid ${quantity} to {user.name} for {reason} (CREDIT)")
            
            user.balance = user.balance + quantity
        except Exception as e:
            print(str(e))

    def add_balance(self, balance: float):
        if balance > 0:
            self.balance += balance

    def add_friend(self, user):
        self.activities.append(f"{self.name} added a new friendship with {user.name}")
        self.friends.append(user)

    def retrieve_activity(self):
        return self.activities


class MiniVenmo:

    def __init__(self):
        self.users = []

    def create_user(self, name: str, balance: float = 0):
        new_user = User(name=name, balance=balance)
        self.users.append(new_user)
        return new_user
    
    def render_feed(self, feed):
        for activity in feed:
            print(activity)


if __name__ == "__main__":
    venmo = MiniVenmo()
    vitor_user = venmo.create_user(name="Vitor", balance=200)
    diego_user = venmo.create_user(name="Diego", balance=200)

    vitor_user.pay(user=diego_user, quantity=-5.00, reason="Coffee")
    diego_user.pay(user=vitor_user, quantity=15.00, reason="Lunch")
    diego_user.pay(user=vitor_user, quantity=300.00, reason="Dinner")

    vitor_user.add_friend(diego_user)
    diego_user.add_friend(vitor_user)
    
    print("Vitor activities")
    vitor_feed = vitor_user.retrieve_activity()
    venmo.render_feed(vitor_feed)

    print("diego activities")
    diego_feed = diego_user.retrieve_activity()
    venmo.render_feed(diego_feed)
