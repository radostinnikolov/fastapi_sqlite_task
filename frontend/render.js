const express = require( "express" ),
  app = express(),
  path = require( "path" ),
  PORT = 5000;

app.use( express.static( 'public' ));

app.get( "/", ( req, res ) => {
  res.sendFile( path.join( __dirname + "/public/main/index.html" ));
});

app.get( "/login", ( req, res ) => {
  res.sendFile( path.join( __dirname + "/public/login/login.html" ));
});

app.get( "/sign-up", ( req, res ) => {
  res.sendFile( path.join( __dirname + "/public/sign-up/sign-up.html" ));
});

app.get( "/portal", ( req, res ) => {
  res.sendFile( path.join( __dirname + "/public/portal/portal.html" ));
});



app.listen( PORT, () => console.log( `API server listening on port ${ PORT }` ) );