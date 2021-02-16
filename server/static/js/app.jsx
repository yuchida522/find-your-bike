"use strict";
function App() {
	return (
		<Router>
        <div><NavComponent/></div>
			<Switch>
				<Route exact path='/login'>
					<Login />
					{/* <Map /> */}
				</Route>

                <Route exact path='/about'>
					<About />
                </Route>

                <Route exact path='/profile'>
				    <Profile />
					{/* <Map /> */}
 				</Route>
                <Route exact path='/navbar'>
                    <NavComponent />
                </Route>
				
			</Switch>
        </Router>
	
    );
}

// // change this to class style 
// // class allows you to have props and attach a state 
// 	// you have to have the state for the login

// 	class App extends React.Component {
// 		constructor(props){
// 		super(props);
// 		}
// 		render() {
// 				return (
// 					<div><h1>TEST STRINGS</h1>
					
// 					<Router> 	
// 						<Switch>
// 							<Route exact path='/login'>
// 								<Login />
// 							</Route>
// 							</Switch>
// 							</Router>
// 					</div>
// 					// <Router>
// 					// <div><NavComponent/></div>
// 					// 	<Switch>
// 					// 		<Route exact path='/login'>
// 					// 			<Login />
// 					// 			<Map />
// 					// 		</Route>
			
// 					// 		<Route exact path='/about'>
// 					// 			<About />
// 					// 		</Route>
			
// 					// 		<Route exact path='/profile'>
// 					// 			<Profile />
// 					// 			<Map />
// 					// 		 </Route>
// 					// 		<Route exact path='/navbar'>
// 					// 			<NavComponent />
// 					// 		</Route>
							
// 					// 	</Switch>
// 					// </Router>
				
// 				);
// 			}
// 		}



ReactDOM.render(<App />, document.getElementById('app'))




