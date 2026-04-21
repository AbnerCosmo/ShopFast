class Payment:
    def __init__(self, amount_paid: float):
        self.amount_paid = amount_paid

    def is_valid(self, total_amount: float) -> bool:
        return self.amount_paid >= total_amount


class Coupon:
    def __init__(self, code: str, discount_percentage: float):
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Cupom inválido")

        self.code = code
        self.discount_percentage = discount_percentage

    def apply(self, amount: float) -> float:
        return amount * (1 - self.discount_percentage / 100)


class Order:
    def __init__(self, total_amount: float):
        self.total_amount = total_amount
        self.final_amount = total_amount
        self.status = "CREATED"

    def apply_coupon(self, coupon: Coupon):
        self.final_amount = coupon.apply(self.final_amount)
        self.status = "PRICED"

    def mark_paid(self):
        self.status = "PAID"

    def mark_failed(self):
        self.status = "FAILED"


class CheckoutService:
    def process_order(self, order: Order, payment: Payment, coupon: Coupon = None) -> bool:

     
        if coupon:
            order.apply_coupon(coupon)

        
        if not payment.is_valid(order.final_amount):
            order.mark_failed()
            raise Exception("Pagamento insuficiente")

        
        order.mark_paid()
        return True
