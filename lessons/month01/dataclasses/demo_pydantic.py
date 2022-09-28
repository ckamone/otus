from pydantic import BaseModel

class Order(BaseModel):
    id: int
    email: str

def main():
    order = Order(id=1, email='test@test.ru')
    print(order.email)

if __name__ == '__main__':
    main()

