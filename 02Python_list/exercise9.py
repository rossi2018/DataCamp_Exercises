areas=["hallway",11.25,"kitchen",18.0,"chill zone",20.0,"bedroom",10.75,"bathroom",10.50,"poolhouse",
24.5,"garage",15.45]

#Remove poolhouse and the corresponding float (24.5)
#del(areas[10]);del(areas[11])
#using the above code with index 10 and 11.If you first remove areas[10],all elements after index move
#up a spot.If you then do del(area[11]), you are deleting the element that was originally at index 12

#this remove poolhouse and 24.5 at once from the areas list 
del(areas[-4:-2])

print(areas)
