testnum <- 600851475143

# We only need factors up to the root, can get the other ones by dividing.
a=c(1:floor(sqrt(testnum)))
smallfactors=a[testnum%%a==0]
bigfactors=testnum/smallfactors

# Get all factors in ascending order, except 1 and the number
allfactors=c(smallfactors[2:length(smallfactors)],rev(bigfactors[2:length(bigfactors)]))

# Get the outer remainder array (every factor%%every factor)
outer_fac=outer(allfactors,allfactors,"%%")

# Biggest prime is the factor with non-zero remainder for every smaller factor.
# Corresponds to the last row in outer_fac with no zero in the lower triangle, so we find that.
filled_upper=outer_fac+upper.tri(outer_fac,diag=TRUE) #Fill in the upper triangle and diagonal
check_zeros=apply(filled_upper,1,prod) # Multiply through the rows to find those with a zero.  A bit lazy.
allfactors[which.max(check_zeros)] #Find the last non-zero and corresponding factor
