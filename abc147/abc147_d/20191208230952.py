
def sumXOR(arr,n): 
      
    sum = 0
    for i in range(0, 65): 
    
        #  Count of zeros and ones 
        zc = 0
        oc = 0
           
        # Individual sum at each bit position 
        idsum = 0
        for j in range(0, n): 
            if (arr[j] % 2 == 0): 
                zc = zc + 1
                  
            else: 
                oc = oc + 1
            arr[j] = arr[j] // 2
          
           
        # calculating individual bit sum  
        idsum = oc * zc * (1 &lt;&lt; i) 
    
        # final sum     
        sum = sum + idsum;  
      
    return sum%(1000000007)
  
  
  
# driver function  
sum = 0
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
sum = sumXOR(arr, n); 
print (sum) 
