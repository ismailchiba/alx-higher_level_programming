#!/usr/bin/node

const request = require(`request`);
const fs = require(`fs`);

if (process.argv.length > 3){
    const Url = process.argv[2];
    const file = process.argv[3];

    request(`${Url}`,(err, res, body) => {
        if(err)
        {
            console.log(err);
        }
        fs.writeFile(`${file}`, body, 'utf8', (err) => {
            if(err)
            {
                console.log(err);
            }
        })
    })
}