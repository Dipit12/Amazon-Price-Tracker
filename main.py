from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9"
}
my_email = "dipitmadan@gmail.com"
password = "fimfcrtsgykutqwu"

response = requests.get(url = product_url,headers=headers)
data = response.text
#print(data)
soup = BeautifulSoup(data,'lxml')
# <span class="aok-offscreen">   $99.95  </span>
price_information = soup.find(name ="span",class_ = "aok-offscreen")

product_price = price_information.getText().strip().split("$")[1]
final_product_price = float(product_price)
# <span id="productTitle" class="a-size-large product-title-word-break">        Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer &amp; Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart       </span>
product_name = soup.find(name ="span", id = "productTitle",class_ = "a-size-large product-title-word-break").getText().strip()
print(product_name)

print(final_product_price)

SET_price = 98
if final_product_price < SET_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dipitgamer1211@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n {product_name} now at {final_product_price}\n{product_url}".encode("utf-8")
        )

""" connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="dipitgamer1211@gmail.com", msg=f"Subject:Amazon price tracker\n\n {product_name} now at {final_product_price} url: {product_url}").encode("utf-8")
    connection.close()
"""






