GooglePlayServicesStripper
==========================

Strips the Google Play Services JAR archive and removes the folders that are specified below.
This should lower the methods count of the final DEX file and should lower the chance of hitting
the (dreaded) 64K methods limit.

What this script does is essentially the following:

 - create a temporary directory to work in
 - Extracts the content of the google-play-services.jar file
 - Based on the content of the 'configuration' var, it removes the desired modules (in the form of directories)
 - Repackages the remaining directories in a google-play-services-STRIPPED.jar file
 - cleans up as needed
 - 
Credits go to:  
 - https://gist.github.com/dextorer/a32cad7819b7f272239b
 - https://medium.com/@rotxed/dex-skys-the-limit-no-65k-methods-is-28e6cb40cf71

