import React, { useEffect, useRef } from 'react';

function TradingViewWidget() {
    const container = useRef();

    useEffect(
        () => {
            if (container.current && !container.current.firstChild) {
                const script = document.createElement("script");
                script.src = "https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js";
                script.type = "text/javascript";
                script.async = true;
                script.innerHTML = `
                {
                  "symbols": [
                    [
                      "CAPITALCOM:GOLD|1D|EUR"
                    ]
                  ],
                  "chartOnly": false,
                  "width": 900,
                  "height": 350,
                  "locale": "fr",
                  "colorTheme": "light",
                  "autosize": false,
                  "showVolume": false,
                  "showMA": false,
                  "hideDateRanges": false,
                  "hideMarketStatus": true,
                  "hideSymbolLogo": true,
                  "scalePosition": "right",
                  "scaleMode": "Normal",
                  "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
                  "fontSize": "10",
                  "noTimeScale": false,
                  "valuesTracking": "1",
                  "changeMode": "price-and-percent",
                  "chartType": "candlesticks",
                  "maLineColor": "#2962FF",
                  "maLineWidth": 1,
                  "maLength": 9,
                  "fontColor": "rgba(14, 23, 44, 1)",
                  "backgroundColor": "rgba(255, 255, 254, 1)",
                  "widgetFontColor": "rgba(14, 23, 44, 1)",
                  "lineType": 0,
                  "dateRanges": [
                    "1d|1",
                    "1w|15",
                    "1m|30",
                    "3m|60",
                    "12m|1D",
                    "60m|1W",
                    "all|1M"
                  ],
                  "downColor": "rgba(255, 39, 102, 1)",
                  "upColor": "rgba(127, 222, 136, 1)",
                  "borderUpColor": "rgba(127, 222, 136, 1)",
                  "borderDownColor": "rgba(255, 39, 102, 1)",
                  "wickUpColor": "rgba(127, 222, 136, 1)",
                  "wickDownColor": "rgba(255, 39, 102, 1)",
                  "dateFormat": "dd/MM/yyyy"
                }`;
            container.current.appendChild(script);
            }

            return () => {
                // Supprimez le script du container
                if (container.current) {
                    while (container.current.firstChild) {
                        container.current.removeChild(container.current.firstChild);
                    }
                }
            };
        },
        []
    );

    return (
        <div className="tradingview-widget-container" ref={container}>
            <div className="tradingview-widget-container__widget"></div>
        </div>
    );
}

export default TradingViewWidget;
