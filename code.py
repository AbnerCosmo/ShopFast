class Payment:
    def __init__(self, amount_paid: float):
        self.amount_paid = amount_paid

    def is_valid(self, total_amount: float) -> bool:
        return self.amount_paid >= total_amount


class Coupon:
    def __init__(self, code: str, discount_percentage: float):
        self.code = code
        self.discount_percentage = discount_percentage

    def apply(self, amount: float) -> float:
        return amount * (1 - self.discount_percentage / 100)


class Order:
    def __init__(self, total_amount: float):
        self.total_amount = total_amount

    def apply_coupon(self, coupon: Coupon) -> float:
        return coupon.apply(self.total_amount)


class CheckoutService:
    def process_order(self, order: Order, payment: Payment, coupon: Coupon = None) -> bool:
        final_amount = order.total_amount

        if coupon:
            final_amount = order.apply_coupon(coupon)

        if not payment.is_valid(final_amount):
            raise Exception("Pagamento insuficiente para concluir o pedido")

        return True  
