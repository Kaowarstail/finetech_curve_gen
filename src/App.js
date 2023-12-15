import React, { useState } from 'react';
import TradingViewWidget from './TradingViewWidget';
import './App.css';
import LogoBlack from './images/Logo_Black.png'

export default function App() {

    const [selectedAction, setSelectedAction] = useState(null);
    const handleDivClick = (actionNumber) => {
        setSelectedAction(actionNumber);
    };

    const tabActionsName= ["Gold", "Ethereum", "Apple", "Microsoft", "Tesla", "Bitcoin"];
    const tabActionsPrice = ["1857.32€", "1857.32€", "1857.32€", "1857.32€", "1857.32€", "1857.32€"];
    const tabActionsVariation = ["+170.25€ (0.45%)", "+170.25€ (0.45%)", "+170.25€ (0.45%)", "+170.25€ (0.45%)", "+170.25€ (0.45%)", "+170.25€ (0.45%)"];
    const tabActionsSymbol = ["CAPITALCOM:GOLD|1D|EUR", "BINANCE:ETHUSD|1D|EUR", "NASDAQ:AAPL|1D|EUR", "NASDAQ:MSFT|1D|EUR", "NASDAQ:TSLA|1D|EUR", "CRYPTO:BTCUSD|1D|EUR"]

    return (
        <body>
            <header>
                <img src={LogoBlack} className="logoHeader" onClick={() => window.location.reload()} alt="Logo de Finsight"/>
                <div className="helloUser">
                    <h2>Hello Maxime !</h2>
                    <p>Belle journée n'est-ce pas ?</p>
                </div>
            </header>
            <main>
                <div className="blocFluxActuel">
                    <div className="fluxActuel">
                        <h2>Flux actuel ·</h2><h3>{tabActionsName[selectedAction]}</h3>
                    </div>
                    <div className="tradingViewWidget">
                        <TradingViewWidget symbol={tabActionsSymbol[selectedAction]}/>
                    </div>
                    <button className="btnGenererPrediction">Générer une prédiction</button>
                </div>
                <div className="blocActions">
                    {[0, 1, 2, 3, 4, 5].map((number) => (
                        <div className={"Actions action" + number + (selectedAction === number ? " selected" : "")}
                            onClick={() => handleDivClick(number)}>

                            <div className="hautAction">
                                <h4 className="actionName">{tabActionsName[number]}</h4>
                                <h4 className="actionOptions">···</h4>
                            </div>
                            <div className="milieuAction">
                                <h4>{tabActionsPrice[number]}</h4>
                            </div>
                            <div className={"basAction "/* + (Math.floor(Math.random() * 2) + 1 == "1" ? "txtVert" : "txtRouge")*/}>
                                <h5>{tabActionsVariation[number]}</h5>
                            </div>
                        </div>
                    ))}
                </div>
                <div className="blocPrediction">
                    <div className="prediction">
                        <h2>Prédiction</h2>
                    </div>
                    <button className="btnExporterPrediction">Exporter la prédiction</button>
                </div>
                <div className="blocProfil">
                    <h2>Mon profil</h2>
                    <p>User number : <span className="bold">CT6763817</span></p>
                    <p>User : <span className="bold">Trader01_QONTO</span></p>
                    <p>Company : <span className="bold">Qonto</span></p>
                    <p>Forfait : <span className="bold">Enterprise</span></p>
                    <p>Niveau d’accès : <span className="bold">A1</span></p>
                    <p>User type : <span className="bold">Operator</span></p>
                    <p>User team : <span className="bold">QONTO_Trader</span></p>
                    <div className="deconnexion">
                        <button className="btnDeconnexion">Se déconnecter</button>
                    </div>
                </div>
            </main>
        </body>
    )
}