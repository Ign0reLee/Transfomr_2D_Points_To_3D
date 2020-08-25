# Transform 2D Points to 3D Points

  Study Repository for 3D points Scaling, using 2D points
  
  Refer to this column : [How to transform a 2D image into a 3D space?](https://towardsdatascience.com/how-to-transform-a-2d-image-into-a-3d-space-5fc2306e3d36)
  
---

# Enviroment

  numpy<br>
  glob<br>
  pandas

---

# How to use it

 **First, Make Directory Named "_New_Data"**

 **Second, Run Code!**

  ```cmd
  python transform.py --path_2d Your2DPointsPATH --path3d Your3DPointsPATH \
  --translate TranslateFactorYouWant \
  --left LeftSliceYouWant \
  --right RightSliceYouWant \
  --os
  ```

  --path_2d   : directory path of 2d points files<br>
  --path_3d   : directory path of 3d points files<br>
  --translate : Translation factor, Default : 30<br>
  --left      : Points Slicer For Left Value<br>
  --right     : Points Slicer For Right Value<br>
  --os        : if use linux, input 'u' or if use windows, input 'w', it just separator for path slicing


---


# WorkFlow
  
  1. Load 3D File and Translate Translat factor(just addition)
    - in the 3D directory must be have 1 file
    - File must be formed like (index, x, y, z)

  2. Load 2D Files and Compute Scaling Factor between 3D points and 2D points, for each files
    - All Files must be formed like (index, x, y)
    - Scaling Factor calculation expression is as follows:
      -  Compute Euclidean Distance Right Minimum Points to Left Maximum Points(on the x-axis)
      -  2D distance were divided into 3D distance
  
  3. Scaling 3D Points using Scaling Factor
    - In now, just compute multiply each.

  