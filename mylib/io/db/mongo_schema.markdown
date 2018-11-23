# Schema

# my object

{
  _id: ObjectID("lskdjf;lksjdf"),
  
*first*time:  ISODate("2013-10-10T23:06:00.000Z"),
  
*last*time: ISODate("2013-10-10T23:06:00.000Z"),

}

{
    _id:ObjectId("6548435135s65df89a6359w86as2v6"),
    speed: {
        0: {0:33,1:34,...},
        1: {0:35,1:35,...}
        ...
        59: {0:22,...59:22}
        },
    ts: ISODate("2013-10-16T22:07:00:00-0500")

}

db.metrics.update(
  { 
    timestamp_minute: ISODate("2013-10-10T23:06:00.000Z"),
    type: â€�memory_usedâ€�
  }, 
  {$set: {â€œvalues.59â€�: 2000000 } }
)

