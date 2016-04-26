#!/usr/bin/php
<?php
  define('API_KEY',   ''); // Grab one from https://developer.forecast.io
  define('LATITUDE',  43.644426);
  define('LONGITUDE', -79.397013);
  define('URL',       'https://api.forecast.io/forecast/');
  define('UNITS',     'units=ca');
  
  $json = file_get_contents(URL . API_KEY . '/' . LATITUDE . ',' . LONGITUDE . '?' . UNITS);
  $response = json_decode($json);
  $temperature = 'It feels like ' . round($response->currently->apparentTemperature) . "C.";
  $conditions = $response->minutely->summary;
  $precipitation = $response->currently->precipProbability . '% chance of precipitation.';
  
  $iconResult = $response->minutely->icon;
  //clear-day, clear-night, rain, snow, sleet, wind, fog, cloudy, partly-cloudy-day, or partly-cloudy-night
  switch ($iconResult) {
    case 'clear-day':
      $icon='☀️';
      break;
    case 'clear-night':
      $icon='🌕';
      break;
    case 'rain':
      $icon='☔️';
      break;
    case 'snow':
      $icon='❄️';
      break;
    case 'sleet':
      $icon='☔️️';
      break;
    case 'wind':
      $icon='💨';
      break;
    case 'cloudy':
      $icon='☁️';
      break;
    case 'partly-cloudy-day':
      $icon='⛅️';
      break;
    case 'partly-cloudy-night':
      $icon='⛅️';
      break;
    default:
      $icon='';
  }
  
  
  $output = $icon . '  ' . $temperature . ' ' . $conditions . ' ' . $precipitation;
  
  $stdout = fopen("php://stdout", "w");
  fwrite( $stdout, $output);
  fclose( $stdout );
