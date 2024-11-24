
# [Your Website Name]

Code Institute Portfolio Project - Clothing E-Commerce Website

[View deployed site](#) <!-- Replace # with your live site link -->

![amiresponsive](static/images/amiresponsive.png) <!-- Replace with an actual image of your site -->

**A fashion-forward experience**

Our website is designed to offer users a seamless experience shopping for t-shirts and shoes. With a clear and intuitive design, customers can easily browse products, add items to their cart, and securely complete their purchases. The platform ensures an enjoyable and safe online shopping experience.

---

## Features

### Existing Features

#### Product Browsing

- **Category Navigation:** Users can explore categories like t-shirts and shoes with ease. <!-- Add more categories as your inventory expands -->
- **Search Functionality:** Users can search for products by name or keyword to quickly find what they need.
- **Detailed Product Pages:** Includes high-quality images, descriptions, prices, and available sizes for each product.

#### Shopping Cart and Checkout

- **Cart Management:** Add, edit, or remove items from the cart.
- **Checkout Process:** A streamlined process to review items, enter shipping details, and pay securely via credit card. <!-- Extend payment options as needed -->

#### User Accounts

- **User Registration and Login:** Create an account to save purchase history and streamline future purchases.
- **Order Tracking:** Users can view the status of their current orders.
- **Wishlist:** Save products for later.

#### Responsive Design

- Optimized for desktop, tablet, and mobile devices.

#### Security Features

- **Secure Payments:** Protect customer data with encrypted transactions.
- **Password Protection:** User accounts are safeguarded with strong passwords.

---

### Features for the Future

- **Product Reviews:** Allow users to leave reviews and ratings for products.
- **Discount Codes:** Offer promo codes to attract more customers.
- **Multiple Filters:** Enable sorting by size, color, or price range. <!-- Consider adding other filter options as your inventory grows -->
- **Email Notifications:** Send updates on orders and promotional offers.
- **Dark/Light Mode Toggle:** Users can switch between light and dark themes for better accessibility.

---

## Accessibility

Our website prioritizes accessibility by offering:
- High contrast colors for better readability.
- Large buttons and touch-friendly design.
- Alt text for all images to support screen readers.

### Accessibility Testing

- **WAVE Web Accessibility Evaluation Tool:** Confirmed compliance with basic accessibility standards.
- **Google Lighthouse:** Achieved high scores for performance and accessibility.

---

## Design

### Wireframes

<details>
    <summary>Home Page</summary>
    <img src="docs/wireframes/home.png"> <!-- Replace with your wireframe image -->
</details>

<details>
    <summary>Product Page</summary>
    <img src="docs/wireframes/product.png"> <!-- Replace with your wireframe image -->
</details>

<details>
    <summary>Checkout Page</summary>
    <img src="docs/wireframes/checkout.png"> <!-- Replace with your wireframe image -->
</details>

---

# User Stories

| ID  | User Story                                                                                     |
|-----|------------------------------------------------------------------------------------------------|
| 1   | As a user, I want to easily browse product categories (t-shirts and shoes) to find what interests me. |
| 2   | As a user, I want to search for a specific product by name or reference to save time.          |
| 3   | As a user, I want to see clear photos and detailed descriptions of products to better understand what I am buying. |
| 4   | As a user, I want to see the prices of products clearly displayed to make an informed choice.  |
| 5   | As a user, I want to add items to my cart to complete my purchase later.                       |
| 6   | As a user, I want to edit or remove items from my cart before proceeding to checkout.          |
| 7   | As a user, I want to create an account to save my information and purchase history.            |
| 8   | As a user, I want to place an order without creating an account for a faster experience.       |
| 9   | As a user, I want to choose a credit card as my payment method to finalize my purchases.       |
| 10  | As a user, I want to receive a confirmation email after placing an order to ensure my order has been received. |
| 11  | As a user, I want to track the status of my order (in progress, shipped, delivered) to know when it will arrive. |
| 12  | As a user, I want to review my previous orders to check details or reorder items.              |
| 13  | As a user, I want to add products to a wishlist to purchase them later.                        |
| 14  | As a user, I want to read and leave reviews on products to share my experience.                |
| 15  | As a user, I want to benefit from discounts or promo codes to save money on my purchases.      |
| 16  | As a user, I want to see delivery fees clearly displayed before completing my order.           |
| 17  | As a user, I want the website to be accessible on mobile and tablet devices so I can shop wherever I am. |
| 18  | As a user, I want to contact customer service in case of issues or questions about my order.   |
| 19  | As a user, I want to navigate a fast and secure website for a smooth shopping experience.       |
| 20  | As a user, I want to select my size to avoid mistakes when purchasing.                         |

---

## Testing

### Lighthouse Testing

![Lighthouse Desktop](static/images/lighthouse_desktop.png) <!-- Replace with your own test results -->
![Lighthouse Mobile](static/images/lighthouse_mobile.png) <!-- Replace with your own test results -->

### HTML Validator

Validated all HTML templates using [W3C HTML Validator](https://validator.w3.org/).

### CSS Validator

Validated CSS files using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

---

## Deployment

### Steps for Deployment

1. Set up your Django project.
2. Use `Heroku` for deployment.
3. Add the following environment variables:
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `DEBUG` set to `False`.

---

## Tools/Technologies

### Languages

- HTML5
- CSS3
- JavaScript
- Python
- Django

### Frameworks and Libraries

- Bootstrap
- Pillow (for image handling)

---

## Credits

- Icons: [Font Awesome](https://fontawesome.com/)
- Images: [Unsplash](https://unsplash.com/) and [Pexels](https://pexels.com/)

### Disclaimer

This website is for educational purposes only.

