import concurrent.futures
from src.alibaba import alibaba2

class app:
    def __init__(self):
        a=alibaba2.alibab()
        self.a=a
        self.page_links=[]
    
    def get_name_of_search(self,search_text):
        '''
        :what:
            -caller method of alibaba2
        :Duties:
            -call the method of alibaba2.py and gives us a list of page_links 
        :Args:
            - search_text (str): the text that you wanna search

        '''
        return self.a.get_name_of_search(search_text)

    def thread_call(self,page_links):
        '''
        :what:
            -thread 
        :Duties:
            - get `page_links` and run them in parallel drivers and every driver gets product links then gets every product 
            link and get it's characteristics and save them in one big list.
        :َArgs:
            - page_links (list): list of (page and the next pages)
        
        '''
        with concurrent.futures.ThreadPoolExecutor() as executer1:
            results_run=[executer1.submit(self.a.run,page_link) for page_link in page_links]
            results_run_driver=[executer1.submit(self.a.get_links,res.result()) for res in results_run]

        links_pp=[]
        for r1 in results_run_driver:
            links_p=[]
            for r2 in r1.result():
                links_p.append(r2.get_attribute('href'))
            links_pp.append(links_p)
            
        final_links=[]
        for j in range(2):
            links_ppp=[]
            for i in range(len(links_pp)):
                links_ppp.append(links_pp[i][j])
            final_links.append(links_ppp)

        final_results=[]
        for link_list in final_links:
            with concurrent.futures.ThreadPoolExecutor() as executer2:
                results=[executer2.submit(self.a.run,link) for link in link_list]
                results1=[executer2.submit(self.a.get,r.result()) for r in results]
            final_results.append(results1)
            # final_results.append(link_list)
        return final_results



    def save(self,data):
        '''
        :what:
            - saving data
        :Duties:
            - call save_todb method of alibab2.py for every data(of products)
        :Arg:
            - data (list): list that contains of normal_prices,overview,name_func_feature,link,company_detail of all products
        '''
        n=0
        for re in data:
            for ie in re:
                alibaba2.save_todb(ie.result(),n)
                n+=1




search_text=input('Please Enter your desired product')
app1=app()
pages=app1.get_name_of_search(search_text)
res=app1.thread_call(pages)
app1.save(res)
