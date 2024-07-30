#!/usr/bin/node
//Import the fs Module: The fs (file system) module is imported using require('fs')
const fs = require('fs');
//check if the number of command-line arguments is greater than 3
//process.argv[0] is the path to the node.js executable
//process.argv[1] is the path to th file (script file)
//process.argv[2] is the path of the file to write to 
//process.argv[3] is the data to write to the file
if (process.argv.length > 3) {
// Use fs.writeFile to write the data to the specified file
  fs.writeFile(process.argv[2], process.argv[3], 'utf8',
    //callback function to handle any errors 
    err => {
      if (err) {
        //Log the error to the console if it occurs
        console.log(err);
      }
    }
  );
}
