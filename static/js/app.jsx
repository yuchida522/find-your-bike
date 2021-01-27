"use strict";

function App() {
	return (
		<Router>
			<Switch>
				<Route exact path='/login'>
					<Login />
				</Route>
			</Switch>
		</Router>
		
	);
}


ReactDOM.render(<App />, document.getElementById('app'))