ggplot(df[-28,],aes(V1,V3,fill=V1))+geom_bar(stat='identity')+
geom_text(aes(label=V3),hjust=-.1,size=3.2)+
theme(legend.position='none',panel.grid.minor=element_line(colour='white'),panel.background=element_rect(fill='white'))+
theme(axis.line=element_line(colour='black',linetype = 1,size=.8),axis.line.y=element_blank())+
ylab('')+
coord_flip()+
ylim(c(0,45000))+xlab('Chromosome')
