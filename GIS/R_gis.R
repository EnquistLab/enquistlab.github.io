#first, install and run all this stuff, because I said so.  
#Also, it might be useful:

require(rgdal)
require(maptools)
require(mapproj)
require(raster)
require(sp)
require(devtools)
require(taxize)
require(ape)
require(Hmisc)
require(maps)
#although I hate to do it this way, for the sake of this class, let's set our working directory:
setwd("C:/Users/Brian/Desktop/BIEN_API_WORK/test_junk/enquistlab.github.io/GIS/")


#let's start by plotting a basic map using the maps functions.
#just type:

map() #simple as that, since the default is a world map!
map('state')# is another option
#or, if we want it a bit prettier:
map('world',bg = "light blue",col="green",fill=TRUE)#specifying colors is pretty basic, but often helps with visualization

#So, we know what the world looks like, more or less.  Let's see some organisms!

#Let's start by loading a shapefile range map for a randomly chosen species:

cannabis_sativa<-readShapePoly("plant_examples/Cannabis_sativa.shp")#obviously you'll need to change this a bit for your computer
str(cannabis_sativa)#tells us about the structure of the data associated with this map.  Not much here for this simple shapefile,though
cannabis_sativa@proj4string#tells us whether the coordinate reference system is set and whether there is a projection
cannabis_sativa@data#has the species listed.  not very impressive, but useful if you have a lot of maps!
#so, where does this species live?
plot(cannabis_sativa)#not very useful, eh?  try:
map('world',bg = "light blue",col="grey",fill=TRUE)
plot(cannabis_sativa,col="green",add=TRUE)

#hmmm, maybe we want to zoom in on the area where the species is found?

plot(cannabis_sativa,col="green")
map('world',add=TRUE)

#let's try another species:
acer_rubrum<-readShapePoly("plant_examples/Acer_rubrum.shp")
#let's add this one
plot(acer_rubrum,col="dark green", add=TRUE)

#lets plot JUST the areas of overlap
map('world',bg = "light blue",col="grey",fill=TRUE)
plot(gIntersection(acer_rubrum,cannabis_sativa),add=TRUE,col="green")#this maps JUST the areas that are in common between the two


#what about occurrence points?
load("plant_examples/cannabis_sativa_occurrences")

#easy, just add the points as you would with any normal plot
map('world',bg = "light blue",col="grey",fill=TRUE)
plot(cannabis_sativa,col="light green",add=TRUE)
points(cannabis_sativa_occurrences$longitude,cannabis_sativa_occurrences$latitude,pch=16,cex=.25,col="red")


#raster data: climate
bioclim1<-raster("bio_10m_bil/bio1.bil")
#okay, guess how we plot it?
plot(bioclim1)
plot(cannabis_sativa,add=TRUE)
# what if we want to know something about where this plant grows?
cannabis_sativa_bioclim1_values<-extract(bioclim1,cannabis_sativa)#this will retrieve all values of the raster that intersect with the shapefile range map
hist(unlist(cannabis_sativa_bioclim1_values))#we could likewise get the mean, variance, whatever we want

cannabis_sativa_points<-SpatialPoints(na.omit(cbind(cannabis_sativa_occurrences$longitude,cannabis_sativa_occurrences$latitude)))#put the occurrence points into a spatial points file, needed for the extract function
cannabis_sativa_bioclim1_values_points<-extract(bioclim1,cannabis_sativa_points)#this function retreives the values at all points for the spatial points file
hist(cannabis_sativa_bioclim1_values_points)


#IUCN data:combined shapefiles!
caecillians<-readShapePoly("GYMNOPHIONA/GYMNOPHIONA.shp")

#These shapefile have more species associated with them and more metadata, lets take a look!
str(caecillians)
caecillians@data$binomial

#Note that conveniently these shapefiles are in a dataframe, so typical dataframe indexing works with them

plot(caecillians)#plots all shapefiles
map('world',xlim = c(-90,-45),ylim=c(0,15),fill=TRUE,col="light green")
plot(caecillians[1,],col="brown",add=TRUE)#plots only the first shapefile
caecillians[1,]@data$binomial#get the species name for the first shapefile

blank_raster<-setValues(bioclim1,0)
diversity_output<-setValues(blank_raster,0)#create a blank raster to store output data
for(i in 1:length(caecillians)){
  print(i)
  range_i<-caecillians[i,] #extracts the ith range map from the dataframe
  sp_i<-as.character(range_i@data$BINOMIAL) #gets the species associated with the ith range map    
  #rasterized_i<-rasterize(range_i,raster)
  rasterized_i<-rasterize(range_i,blank_raster)
  rasterized_i[which(is.na(getValues(rasterized_i))==TRUE)]<-0
  diversity_output<-diversity_output+rasterized_i
  plot(diversity_output) 
}


plot(getValues(diversity_output)~getValues(bioclim1))

#change
