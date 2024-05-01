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
  const [predictions, setPredictions] = useState([]);
  const [citiesFetched, setCitiesFetched] = useState(true);

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs((values) => ({ ...values, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setCitiesFetched(false);
    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputs),
    });
    const data = await response.json();
    setPredictions(data.predictions);
    setCitiesFetched(true);
  };

  return (
    <div className="App">
      <div className="project-holder">
        <div className="project-title">Using Current U.S. Weather Features to Predict Location</div>
        <div className="cards-container">
          <form className="model-form" onSubmit={handleSubmit}>
            <h1 className="enter-txt">Enter Weather Features</h1>
            <div className="underline-container">
              <div className="label-input-container">
                <div className="icon-label-container">
                  <label className="feature-label" htmlFor="temperature">
                    Temperature (&deg;F)
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
              <div className="label-input-container">
                <div className="icon-label-container">
                  <label className="feature-label" htmlFor="humidity">
                    Humidity (%)
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
              <div className="label-input-container">
                <div className="icon-label-container">
                  <label className="feature-label" htmlFor="dewPoint">
                    Dew Point (&deg;F)
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
              <div className="label-input-container">
                <div className="icon-label-container">
                  <label className="feature-label" htmlFor="precipitation">
                    Precipitation (in)
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
              <div className="label-input-container">
                <div className="icon-label-container">
                  <label className="feature-label" htmlFor="windSpeed">
                    Wind Speed (kt)
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
              <div className="label-input-container">
                <div className="icon-label-container">
                  <label className="feature-label" htmlFor="windDirection">
                    Wind Direction (&deg;)
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
          <div className="predictions-container">
            <h1 className="predicted-title">Predicted Cities</h1>
            <div className="predicted-desc">Ranked by predicted percentage, or how close the entered features are to a city's own features</div>
            {
              !citiesFetched ?
              <div className="loader-holder">
                <div className="loader"></div>
              </div> :
              predictions.map((prediction, index) => (
                <p key={index} className="prediction">{`${index + 1}. ${prediction}`}</p>
              ))
            }
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
