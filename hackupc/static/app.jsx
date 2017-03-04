class Root extends React.Component {
    state = {
        display: 0,
    };

    changeDisplay(screen) {
        console.log(screen);
        this.setState({display : screen})
    }

    render() {
        let st = this.state.display;

        return (
            <div className="container-fluid" style={{height: '100%'}}>
                <div className="row" style={{height: '100%'}}>
                    <div className="col-md-2" style={{height: '100%', 'display': 'table-cell', 'verticalAlign': 'middle'}}>
                        <div className="buttons">
                            <div className="row">

                                <button type="button" className="btn btn-primary" onClick={this.changeDisplay.bind(this, 0)} style={{'marginBottom': '40px', 'marginLeft' : '40px'}}>0</button>
                            </div>
                            <div className="row">
                                <button type="button" className="btn btn-primary" onClick={this.changeDisplay.bind(this, 1)} style={{'marginBottom': '40px', 'marginLeft': '40px'}}>1</button>
                            </div>
                            <div className="row">
                                <button type="button" className="btn btn-primary" onClick={this.changeDisplay.bind(this, 2)} style={{'marginBottom': '40px', 'marginLeft': '40px'}}>2</button>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-10">
                        <h1> hello, {st} </h1>
                    </div>
                </div>
            </div>
        );
    }
}

ReactDOM.render(
    <Root />,
    document.getElementsByClassName('root')[0]
);