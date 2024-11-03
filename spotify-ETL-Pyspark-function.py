import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node track
track_node1730538633905 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-proj-datestorage/Staging/track.csv"], "recurse": True}, transformation_ctx="track_node1730538633905")

# Script generated for node artist
artist_node1730538633148 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-proj-datestorage/Staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1730538633148")

# Script generated for node album
album_node1730538630441 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-proj-datestorage/Staging/albums.csv"], "recurse": True}, transformation_ctx="album_node1730538630441")

# Script generated for node artist-album
artistalbum_node1730538747649 = Join.apply(frame1=album_node1730538630441, frame2=artist_node1730538633148, keys1=["artist_id"], keys2=["id"], transformation_ctx="artistalbum_node1730538747649")

# Script generated for node Join withtrack
Joinwithtrack_node1730538826158 = Join.apply(frame1=artistalbum_node1730538747649, frame2=track_node1730538633905, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtrack_node1730538826158")

# Script generated for node Drop Fields
DropFields_node1730538933691 = DropFields.apply(frame=Joinwithtrack_node1730538826158, paths=["id", "`.track_id`"], transformation_ctx="DropFields_node1730538933691")

# Script generated for node DestinationData
DestinationData_node1730538969763 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1730538933691, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotify-proj-datestorage/Datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="DestinationData_node1730538969763")

job.commit()
