# babali
### All of three python files must be in the same directory ###
### you should run program from alibaba2.py ###
### alibaba2.py contain (alibab) Class and it has two functions ### 
### run_driver ###
`def run_driver(self,search_txt):`the first function get search input and run chrome driver and open the link of search result
### run ###
`def run(self):` if we call second function (run) after sometimes we have all the infomation from alibaba.com according to search text
`links_of_all_product=p.link_title_of_all_product(self.driver)[0]` call product class and get all of products links and saving them

This function (run) has a for loop.So this loop call (product) class and (company) class in every iteration and save the return results from these two class in some variable

`(if i ==3) : break` The variable (i) in loop specifies how many of the first results to scrap ... If we want 4 of the first results we can set 3  in code

`normal_prices=products.price_normalizer(prices)`
`name_func_feature=products.name_func_feature(overview[0],title_of_all_product)`
After loop we call some function from products.py to normalize price and get (name or feature or function) of product beacuase the price have some additional words and it is 
float ... normalizer give us float and clean price ... we also need short name and feature and function. So those two lines code give us our needs.
## saving ##
`def save_todb(result):`
after class(alibab) we have save_todb function that should call after getting data from site.this piece of code get all the information (that we scraped) and save them in mongodb atlass (virtual database) in two collections(Company & Products)

There were challenges in getting the price and the year of establishment, which was achieved by trial and error
