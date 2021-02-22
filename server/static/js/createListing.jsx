'use strict';


function CreateListing () {
	// const [uploadImageState, setUploadImageState] = React.useState('');
	const [image, setImage] = React.useState('');
	const [title, setTitle] = React.useState('');
	const [description, setDescription] = React.useState('');
	const [conditionNew, setConditionNew] = React.useState(false);
	const [conditionUsed, setConditionUsed] = React.useState(false);
	const [price, setPrice] = React.useState('');
	const [bikeType, setBikeType] = React.useState('');


	const myWidget = cloudinary.createUploadWidget({cloudName:'online-bike-exchange', upload_preset:'g3w96a71',}, 
						(error, result) => {if (result.event == "success") {
							setImage(result.info.url)
						}});
	
	const checkedBoxes = new Set()
	
	function handleTitleChange(evt) {
		setTitle(evt.target.value)
	};

	function handleDescriptionChange(evt) {
		setDescription(evt.target.value)
	};

	function handlePriceChange(evt) {
		setPrice(evt.target.value)
	}

	function handleBikeTypeChange(evt) {
		setBikeType(evt.target.value)
	}
	
	return (
    <React.Fragment>
			<h1>Create Listing</h1>
			<Form>
				<Form.Group as={Row} controlId="listingTitle">
					<Form.Label column sm="2">
						Title
					</Form.Label>
					<Col sm="10">
						<Form.Control type="text" placeholder="Title" value={title} onChange={handleTitleChange}/>
					</Col>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingPhotos">
					<Form.Label column sm="2">
						Images
					</Form.Label>
					<Col sm="10">
						<Image id="upload-image" src={image}></Image>
						<Button id="upload-image-btn" onClick={()=> {myWidget.open()}}>Upload Images</Button>
					</Col>
				</Form.Group>
				<Form.Group as={Row} controlId="listingDescription">
					<Form.Label column sm="2">
						Description
					</Form.Label>
					<Col sm="10">
						<Form.Control as="textarea" rows={3} placeholder="Description" value={description} onChange={handleDescriptionChange}/>
					</Col>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingCondition">
					<Form.Label column sm="2">
						Condition
					</Form.Label>
						<Form.Check inline label="New" value="new"  id="new-condition" type="checkbox" />
						<Form.Check inline label="Used" value="used" id="used-condition" type="checkbox" />
  			</Form.Group>
				<Form.Group as={Row} controlId="listingType">
					<Form.Label column sm="2">
						Listing Type
					</Form.Label>
						<Form.Check inline label="For sale" value="sale" type="checkbox" />
						<Form.Check inline label="For trade" value="trade" type="checkbox" />
						<Form.Check inline label="For free" value="free" type="checkbox" />
  			</Form.Group>
				<Form.Group as={Row} controlId="listingPrice">
					<Form.Label column sm="2">
						Price
					</Form.Label>
					<Col sm="7">
						<Form.Control type="text" placeholder="required" value={price} onChange={handlePriceChange}/>
					</Col>
  			</Form.Group>
					<Row>
						<Form.Label column sm="2">
							Bike Type
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" value={bikeType} onChange={handleBikeTypeChange}/>
						</Col>
						<Form.Label column sm="2">
							Model
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>		
  				</Row>
					<Row>
						<Form.Label column sm="2">
							Brand
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>
						<Form.Label column sm="2">
							Frame type
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>		
  				</Row>
					<Row>
					<Form.Label column sm="2">
						Frame size
					</Form.Label>
					<Col sm="3">
						<Form.Control type="text" placeholder="required" />
					</Col>		
  				</Row>	
				<Form.Group as={Row} id="listingSubmitBtnGroup">
				<Col sm={{ span: 10, offset: 7 }}>
				<Button id="submit-listing-btn" type="submit">Create Listing</Button>
				</Col>	
				</Form.Group>
			</Form>
    </React.Fragment>
	);
}