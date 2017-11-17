package com.example.jayanth.conductorlocation;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.support.v4.content.ContextCompat;
import android.util.Log;
import android.widget.Toast;

import com.google.android.gms.location.LocationListener;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.TimeZone;
import java.util.concurrent.ExecutionException;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback,
        GoogleApiClient.ConnectionCallbacks,
        GoogleApiClient.OnConnectionFailedListener,
        LocationListener {

    private GoogleApiClient mGoogleApiClient;
    private GoogleMap mMap;
    private FusedLocationProviderClient mFusedLocationClient;
    public static final int REQUEST_LOCATION = 99;
    private LocationRequest mLocationRequest;
    private Marker mCurrLocationMarker;
    private String mLastUpdateTime;
    private Location mCurrentLocation;
    private static float MAP_ZOOM_LEVEL = 17.5f;
    DatabaseReference myRef;
    private float time;
    private float distancetoNITK;
    FirebaseDatabase database;
    private String MYTAG = "HEY";
    private Integer latest=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        database = FirebaseDatabase.getInstance();//"https://location-tracking-44232.firebaseio.com/"
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
        myRef = database.getReference("LocationOfConductor");//"LocationOfConductor"
        myRef.removeValue();
    }

    protected synchronized void buildGoogleApiClient() {
        mGoogleApiClient = new GoogleApiClient.Builder(this)
                .addConnectionCallbacks(this)
                .addOnConnectionFailedListener(this)
                .addApi(LocationServices.API)
                .build();
        mGoogleApiClient.connect();
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
                    REQUEST_LOCATION);
        } else {
            buildGoogleApiClient();
            mMap.setMyLocationEnabled(true);
        }
    }

    @Override
    public void onConnected(@Nullable Bundle bundle) {
        mMap.setMyLocationEnabled(true);

        mLocationRequest = new LocationRequest();
        mLocationRequest.setInterval(10000);
        mLocationRequest.setFastestInterval(10000);
        mLocationRequest.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);

        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.ACCESS_FINE_LOCATION)
                == PackageManager.PERMISSION_GRANTED) {
            LocationServices.FusedLocationApi.requestLocationUpdates(mGoogleApiClient, mLocationRequest, this);
        }

    }

    @Override
    public void onConnectionSuspended(int i) {

    }

    @Override
    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {

    }

    @Override
    public void onPause() {
        super.onPause();

        //stop location updates when Activity is no longer active
        if (mGoogleApiClient != null) {
            LocationServices.FusedLocationApi.removeLocationUpdates(mGoogleApiClient, this);
        }
    }

    @Override
    public void onLocationChanged(Location location) {
        mCurrentLocation = location;
        if (mCurrLocationMarker != null) {
            mCurrLocationMarker.remove();
        }
        float speed;
        Location locationNITK = new Location(location);
        locationNITK.setLatitude(12.9141);
        locationNITK.setLongitude(74.8560);

//        Location locationNITK = new Location(location);
//        locationNITK.setLatitude(12.9807);
//        locationNITK.setLongitude(74.8031);

        distancetoNITK = location.distanceTo(locationNITK) + 10000.0f;
        if (location.getSpeed() < 15.0) {
            speed = 47000.0f / 60.0f; //Speed in meters/min
        }

        else{
            speed = location.getSpeed();
        }

        //Log.d(MYTAG,"Speed is: " + speed );
        //Log.d(MYTAG, "Time is: "+ time);
        time = distancetoNITK/speed;
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        dateFormat.setTimeZone(TimeZone.getTimeZone("IST"));
        Date date = new Date();
        mLastUpdateTime = dateFormat.format(date);
        saveToFirebase();

        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());
        MarkerOptions markerOptions = new MarkerOptions();
        markerOptions.position(latLng);
        markerOptions.title("My Current Position");
        markerOptions.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_BLUE));
        mCurrLocationMarker = mMap.addMarker(markerOptions);
        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(latLng, MAP_ZOOM_LEVEL));

    }

    private void saveToFirebase() {
        //myRef.removeValue();
        Map mLocations = new HashMap();
        mLocations.put("Timestamp", mLastUpdateTime);
        Map mCoordinate = new HashMap();
        mCoordinate.put("Latitude", mCurrentLocation.getLatitude());
        mCoordinate.put("Longitude", mCurrentLocation.getLongitude());
        mLocations.put("Location", mCoordinate);
        mLocations.put("Time",time);
        mLocations.put("Distance to Mangalore", distancetoNITK);
        try {
            String temp = "E" + latest.toString();
            latest++;
            myRef.child(temp).setValue(mLocations);
            Toast.makeText(getApplicationContext(), "ADDED TO FIREBASE", Toast.LENGTH_LONG).show();
        }catch(Exception e){
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "NOT ADDED", Toast.LENGTH_LONG).show();
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        mMap.setMyLocationEnabled(true);
        switch (requestCode) {
            case REQUEST_LOCATION: {
                // If request is cancelled, the result arrays are empty.
                if (grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    // Permission was granted
                    if (ContextCompat.checkSelfPermission(this,
                            Manifest.permission.ACCESS_FINE_LOCATION)
                            == PackageManager.PERMISSION_GRANTED) {

                        if (mGoogleApiClient == null) {
                            buildGoogleApiClient();
                        }
                    }

                } else {
                    // Permission was denied
                    Toast.makeText(this, "Permission Denied", Toast.LENGTH_LONG).show();
                }
                return;
            }
        }
    }
}