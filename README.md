GooglePlayServicesStripper
==========================

Strips the Google Play Services JAR archive and removes the folders that are specified below.
This should lower the methods count of the final DEX file and should lower the chance of hitting
the (dreaded) 64K methods limit.

What this script does is essentially the following:

 - Extracts the content of the google-play-services.jar file
 - Checks if strip.conf already exists: if so, it uses that configuration, otherwise it creates one by reading all the modules from the Play Services library
 - Based on the strip.conf content, it removes the desired modules (in the form of directories)
 - Repackages the remaining directories in a google-play-services-STRIPPED.jar file
  
Credits go to:  
 - https://gist.github.com/dextorer/a32cad7819b7f272239b
 - https://medium.com/@rotxed/dex-skys-the-limit-no-65k-methods-is-28e6cb40cf71

