'use strict';

function CreateListing () {
	// const [uploadImageState, setUploadImageState] = React.useState('');
	const [image, setImage] = React.useState('');
	const [title, setTitle] = React.useState('');
	const [description, setDescription] = React.useState('');
	const [condition, SetCondition] = React.useState('')
	const [saleType, setSaleType] = React.useState('')
	const [price, setPrice] = React.useState('');
	const [bikeType, setBikeType] = React.useState('');
	const [brand, setBrand] = React.useState('')
	const [frameSize, setFrameSize] = React.useState('')
	const [frameType, setFrameType] = React.useState('')
	const [model, setModel] = React.useState('')
	const history = useHistory()
	const myWidget = cloudinary.createUploadWidget({cloudName:'online-bike-exchange', upload_preset:'g3w96a71',}, 
						(error, result) => {if (result.event == 'success') {
							setImage(result.info.url)
						}});
	
	function handleSubmit(evt) {
		evt.preventDefault();
		const priceFloat = parseFloat(price)
		const frameSizeInt = parseInt(frameSize)
		let data = {image: image,
								title: title,
								description: description,
								condition: condition,
								saleType: saleType,
								price: priceFloat,
								bikeType: bikeType,
								brand: brand,
								frameSize: frameSizeInt,
								model: model}
		console.log(data)
	}
	function handleCheckboxSaleType(evt) {
		setSaleType(evt.target.value)
	};
	
	function handleCheckboxCondition(evt) {
		SetCondition(evt.target.value)
	};
	
	console.log(title)
	return (
    <React.Fragment>
			<h1>Create Listing</h1>
			<Form>
				<Form.Group as={Row} controlId="listingTitle">
					<Form.Label column sm="2">
						Title
					</Form.Label>
					<Col sm="10">
						<Form.Control type="text" placeholder="Title" value={title} onChange={(evt) => setTitle(evt.target.value)}/>
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
						<Form.Control as="textarea" rows={3} placeholder="Description" value={description} onChange={(evt) => setDescription(evt.target.value)}/>
					</Col>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingCondition">
					<Form.Label column sm="2">
						Condition
					</Form.Label>
						<Form.Check inline label="New" value="new"  id="new-condition" type="checkbox" onChange={handleCheckboxCondition}/>
						<Form.Check inline label="Used" value="used" id="used-condition" type="checkbox" onChange={handleCheckboxCondition}/>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingType">
					<Form.Label column sm="2">
						Listing Type
					</Form.Label>
						<Form.Check inline label="For sale" value="sale" type="checkbox" onChange={handleCheckboxSaleType}/>
						<Form.Check inline label="For trade" value="trade" type="checkbox" onChange={handleCheckboxSaleType}/>
						<Form.Check inline label="For free" value="free" type="checkbox" onChange={handleCheckboxSaleType}/>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingPrice">
					<Form.Label column sm="2">
						Price
					</Form.Label>
					<Col sm="7">
						<Form.Control type="text" value={price} onChange={(evt) => setPrice(evt.target.value)} placeholder="No dollar sign, ex. 3500"/>
					</Col>
  			</Form.Group>
					<Row>
						<Form.Label column sm="2">
							Bike Type
						</Form.Label>
						<Col sm="3">
							<Form.Control as="select" value={bikeType} onChange={(evt) => setBikeType(evt.target.value)}>
								<option selected>Choose...</option>
								<option>Road</option>
								<option>Mountain</option>
								<option>Gravel</option>
								<option>Touring</option>
								<option>Cruiser</option>
								<option>Hybrid</option>
								<option>Electric</option>
								<option>Other</option>
							</Form.Control>
						</Col>
						<Form.Label column sm="2">
							Model
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" value={model} onChange={(evt) => setModel(evt.target.value)}/>
						</Col>		
  				</Row>
					<Row>
						<Form.Label column sm="2">
							Brand
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text"  placeholder="required" value={brand} onChange={(evt) => setBrand(evt.target.value)}/>
						</Col>
						<Form.Label column sm="2">
							Frame type
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" value={frameType} onChange={(evt) => setFrameType(evt.target.value)} />
						</Col>		
  				</Row>
					<Row>
					<Form.Label column sm="2">
						Frame size
					</Form.Label>
					<Col sm="3">
						<Form.Control type="text" value={frameSize} placeholder="required" onChange={(evt) => setFrameSize(evt.target.value)}/>
					</Col>		
  				</Row>	
				<Form.Group as={Row} id="listingSubmitBtnGroup">
				<Col sm={{ span: 10, offset: 7 }}>
				<Button id="submit-listing-btn" onClick={handleSubmit} type="submit">Create Listing</Button>
				</Col>	
				</Form.Group>
			</Form>
    </React.Fragment>
	);
}