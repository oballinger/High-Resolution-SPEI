// Load grid shapefile and climate data
var regions = ee.FeatureCollection("users/ollie/Grid10km")
var dataset = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE')
              .filter(ee.Filter.date('1985-01-01', '2018-02-01'))

// Select precipitation and evapotranspiration           
var precip=dataset.select('pr')
var pet=dataset.select('pet')


// Create function to convert dataset into stacked image 
var rename_band = function(img){
    return img.select([0], [img.id()])};

// Trim images and iterate over dates
var image1 = precip.map(rename_band).toBands().clip(regions);
var image2 = pet.map(rename_band).toBands().clip(regions);

// Compute water balance for the whole sample (precipitation-evapotranspiration)
var diff= image1.subtract(image2)


// Define function to calculate zonal statistics for each grid-cell
var zonalstats = function(collection, regions, level, filename){
    var scale = collection.first().projection().nominalScale();
    var mean = ee.Image(collection)
                       .reduceRegions({collection: regions, reducer: 
                       ee.Reducer.mean()});
    var mean1 = mean.select(['.*'],null,false);
    var file=filename
    var levels=level

    return 
       Export.table.toDrive({
              collection: mean1, 
              description: level+"_Mean_"+file, 
              fileNamePrefix: level+"_Mean_"+file,
              fileFormat: 'CSV'
})}


zonalstats(diff, regions, 'Grid_10km', "WaterBalance")