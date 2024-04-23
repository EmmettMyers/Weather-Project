import React, { useState } from "react";
import "./App.css";
import { FaTemperatureLow } from "react-icons/fa";
import { FaTemperatureQuarter } from "react-icons/fa6";
import { FaDroplet } from "react-icons/fa6";
import { IoRainyOutline } from "react-icons/io5";
import { FaWind } from "react-icons/fa";
import { GiPaperWindmill } from "react-icons/gi";

function App() {
  const [inputs, setInputs] = useState({});
  const [prediction, setPrediction] = useState("");

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs((values) => ({ ...values, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputs),
    });
    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div className="App">
      <form className="model-form" onSubmit={handleSubmit}>
        <h1>Enter Your Values Below</h1>
        <div className="underline-container">
          <div class="label-input-container">
            <div class="icon-label-container">
              <label className="feature-label" htmlFor="temperature">
                Temperature
              </label>
              <FaTemperatureQuarter />
            </div>
            <input
              required
              id="temperature"
              name="temperature"
              value={inputs.temperature || ""}
              onChange={handleChange}
            />
          </div>
          <div className="underline" />
        </div>
        <div className="underline-container">
          <div class="label-input-container">
            <div class="icon-label-container">
              <label className="feature-label" htmlFor="humidity">
                Humidity
              </label>
              <FaDroplet />
            </div>
            <input
              required
              id="humidity"
              name="humidity"
              value={inputs.humidity || ""}
              onChange={handleChange}
            />
          </div>
          <div className="underline" />
        </div>

        <div className="underline-container">
          <div class="label-input-container">
            <div class="icon-label-container">
              <label className="feature-label" htmlFor="dewPoint">
                Dew Point
              </label>
              <FaTemperatureLow />
            </div>
            <input
              required
              id="dewPoint"
              name="dewPoint"
              value={inputs.dewPoint || ""}
              onChange={handleChange}
            />
          </div>
          <div className="underline" />
        </div>

        <div className="underline-container">
          <div class="label-input-container">
            <div class="icon-label-container">
              <label className="feature-label" htmlFor="precipitation">
                Precipitation
              </label>
              <IoRainyOutline />
            </div>
            <input
              required
              id="precipitation"
              name="precipitation"
              value={inputs.precipitation || ""}
              onChange={handleChange}
            />
          </div>
          <div className="underline" />
        </div>

        <div className="underline-container">
          <div class="label-input-container">
            <div class="icon-label-container">
              <label className="feature-label" htmlFor="windSpeed">
                Wind Speed
              </label>
              <FaWind />
            </div>
            <input
              required
              id="windSpeed"
              name="windSpeed"
              value={inputs.windSpeed || ""}
              onChange={handleChange}
            />
          </div>
          <div className="underline" />
        </div>

        <div className="underline-container">
          <div class="label-input-container">
            <div class="icon-label-container">
              <label className="feature-label" htmlFor="windDirection">
                Wind Direction
              </label>
              <GiPaperWindmill />
            </div>
            <input
              required
              id="windDirection"
              name="windDirection"
              value={inputs.windDirection || ""}
              onChange={handleChange}
            />
          </div>
          <div className="underline" />
        </div>

        <button className="predict-button" type="submit">
          Predict
        </button>
      </form>
      <div class="predictions-container">
        <h1>Predictions</h1>
        {prediction && <p className="prediction"> {prediction}</p>}
      </div>
    </div>
  );
}

export default App;
