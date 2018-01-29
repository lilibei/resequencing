library(mapdata)
library(maps)
map('china',fill=0,col='black',mar=c(0,0,0,0))
for(i in 1:136){points(df$x[i],df$y[i],col='red',pch=20)}
