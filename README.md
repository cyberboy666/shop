# shop [WIP]

a custom low-cost online shop for managing and selling some circuits

the idea is to create an open and 'serverless' inventory and payment process for my personal website using [github-pages](https://pages.github.com/), [stripe](http://stripe.com/) and [chalice](https://github.com/aws/chalice).

## flow

- the static __shop__ page will read and display product infomation from a _public yaml file_
- users will select the products they want and click _checkout_ triggering a request to the __chalice service__
- the __chalice service__ will create a payment using __stripe api__ and redirect users to _secure checkout screen_ (which will also collect address info etc)
- if payment is succesful the __chalice service__ will receive a _webhook_ from __stripe__ confirming the purchace and update the _public yaml file_

## inventory

- each _product_ in the inventory is made up of _components_.
- the _availaibe_products_list_ can be calculated dynamically from the _availble_components_list_ and the _product_descriptions_
- if there are mulitple products using the same limited part the user should be able to select either but not both to order
- should be an easy way for me to define new products and edit the amount of components/products in stock
- should be some kind of alert to me if a part is out of stock

