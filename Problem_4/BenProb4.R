ispalindrome <- function(x,maxdigits){
  a=c(1:maxdigits)
  b=10^a
  t1=x%%b
  t2=diff(c(0,t1))*10/b
  t3=t2[1:max(which(t2!=0))]
  if(all(t3==rev(t3))) {
    return(TRUE)
  }
  else return(FALSE)
}

a=c(100:999)
outer_a=a%o%a
all_prods=c(outer_a*lower.tri(outer_a,diag=TRUE))
shortprods=all_prods[all_prods!=0]
max(shortprods*sapply(shortprods,ispalindrome,maxdigits=6))