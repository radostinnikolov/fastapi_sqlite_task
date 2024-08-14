const express = require( "express" ),
  app = express(),
  path = require( "path" ),
  PORT = 5000;

app.use( express.static( 'public' ));

app.get( "/", ( req, res ) => {
  res.sendFile( path.join( __dirname + "/public/index.html" ));
});

app.listen( PORT, () => console.log( `API server listening on port ${ PORT }` ) );