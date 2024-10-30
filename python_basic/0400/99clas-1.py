vw.ol3.MapOptions = {
      basemapType: vw.ol3.BasemapType.GRAPHIC
    , controlDensity: vw.ol3.DensityType.EMPTY
    , interactionDensity: vw.ol3.DensityType.BASIC
    , controlsAutoArrange: true
    , homePosition: vw.ol3.CameraPosition
    , initPosition: vw.ol3.CameraPosition
   }; 
      
  vmap = new vw.ol3.Map("vmap",  vw.ol3.MapOptions);