"""Auto-generated models for BrandStorePages from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class HorizontalPosition(StrEnum):
    """HorizontalPosition Description `LEFT` Left position `CENTER` Center position `RIGHT` Right position"""

    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class StoreBleedImageType(StrEnum):
    """StoreBleedImageType Description `NONE` No image bleed `SIDE` Side image bleed `CORNER` Corner image bleed `ALL` All sides image bleed"""

    ALL = "ALL"
    CORNER = "CORNER"
    NONE = "NONE"
    SIDE = "SIDE"


class StoreCallToActionType(StrEnum):
    """StoreCallToActionType Description `LINK` Link type call to action `BUTTON` Button type call to action"""

    BUTTON = "BUTTON"
    LINK = "LINK"


class StoreColorPalette(StrEnum):
    """StoreColorPalette Description `DEFAULT` Default color scheme `DEFAULT_INVERTED` Inverted default color scheme `SOLID_WHITE` Solid white color scheme `SOLID_BLACK` Solid black color scheme `TRANSLUCENT_WHITE` Translucent white color scheme `TRANSLUCENT_BLACK` Translucent black color scheme `TRANSPARENT_BLACK` Transparent black color scheme `TRANSPARENT_WHITE` Transparent white color scheme"""

    DEFAULT = "DEFAULT"
    DEFAULT_INVERTED = "DEFAULT_INVERTED"
    SOLID_BLACK = "SOLID_BLACK"
    SOLID_WHITE = "SOLID_WHITE"
    TRANSLUCENT_BLACK = "TRANSLUCENT_BLACK"
    TRANSLUCENT_WHITE = "TRANSLUCENT_WHITE"
    TRANSPARENT_BLACK = "TRANSPARENT_BLACK"
    TRANSPARENT_WHITE = "TRANSPARENT_WHITE"


class StoreDealsMode(StrEnum):
    """StoreDealsMode Description `BULK` Bulk mode `AUTOMATIC` Automatic mode"""

    AUTOMATIC = "AUTOMATIC"
    BULK = "BULK"


class StoreImageLayout(StrEnum):
    """StoreImageLayout Description `COVER` Cover layout `CONTAIN` Contain layout `TEXT` Text layout"""

    CONTAIN = "CONTAIN"
    COVER = "COVER"
    TEXT = "TEXT"


class StoreImageShape(StrEnum):
    """StoreImageShape Description `SQUARE` Square shape"""

    SQUARE = "SQUARE"


class StoreImageTextAlign(StrEnum):
    """StoreImageTextAlign Description `LEFT` Left text alignment `RIGHT` Right text alignment"""

    LEFT = "LEFT"
    RIGHT = "RIGHT"


class StoreImageWithTextTileVariation(StrEnum):
    """StoreImageWithTextTileVariation Description `IMAGE_WITH_TEXT` Image with text variation"""

    IMAGE_WITH_TEXT = "IMAGE_WITH_TEXT"


class StoreLayoutType(StrEnum):
    """StoreLayoutType Description `DEFAULT` Default layout configuration `SHOWCASE` Showcase layout configuration for featured display"""

    DEFAULT = "DEFAULT"
    SHOWCASE = "SHOWCASE"


class StorePageTemplate(StrEnum):
    """StorePageTemplate Description `PRODUCT_GRID` Template displaying products in a grid layout `HIGHLIGHT` Template for highlighting specific content `MARQUEE` Template featuring a prominent marquee section `BLANK` Empty template for custom layouts `PRODUCT_COLLECTION` Template for displaying collections of products"""

    BLANK = "BLANK"
    HIGHLIGHT = "HIGHLIGHT"
    MARQUEE = "MARQUEE"
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    PRODUCT_GRID = "PRODUCT_GRID"


class StorePageType(StrEnum):
    """StorePageType Description `BRAND_STORE_PAGE` Standard brand store page that allows customization to show case the brand and product `LANDING_PAGE` Landing page for specific ads program with predefined template"""

    BRAND_STORE_PAGE = "BRAND_STORE_PAGE"
    LANDING_PAGE = "LANDING_PAGE"


class StoreProductCarouselSearchType(StrEnum):
    """StoreProductCarouselSearchType Description `RECOMMENDATION_FOR_YOU` Personalized recommendations `BEST_SELLING` Best selling items"""

    BEST_SELLING = "BEST_SELLING"
    RECOMMENDATION_FOR_YOU = "RECOMMENDATION_FOR_YOU"


class StoreProductSelectorButtonColor(StrEnum):
    """StoreProductSelectorButtonColor Description `WHITE` White button color `BLACK` Black button color `TRANSPARENT` Transparent button color"""

    BLACK = "BLACK"
    TRANSPARENT = "TRANSPARENT"
    WHITE = "WHITE"


class StoreProductSelectorImageLayout(StrEnum):
    """StoreProductSelectorImageLayout Description `TOP` Top image layout `LEFT` Left image layout `RIGHT` Right image layout `BOTTOM` Bottom image layout"""

    BOTTOM = "BOTTOM"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    TOP = "TOP"


class StoreShoppableTextOption(StrEnum):
    """StoreShoppableTextOption Description `TEXT_UNDER_INTERACTIVE_IMAGE` Text under interactive image `NO_TEXT_UNDER_INTERACTIVE_IMAGE` No text under interactive image `TEXT_OVER_IMAGE` Text over interactive image"""

    NO_TEXT_UNDER_INTERACTIVE_IMAGE = "NO_TEXT_UNDER_INTERACTIVE_IMAGE"
    TEXT_OVER_IMAGE = "TEXT_OVER_IMAGE"
    TEXT_UNDER_INTERACTIVE_IMAGE = "TEXT_UNDER_INTERACTIVE_IMAGE"


class StoreSlideType(StrEnum):
    """StoreSlideType Description `IMAGE` Slide type for StoreGallerySlide, StoreImageSlide `ASIN` Slide type for StoreASINSlide"""

    ASIN = "ASIN"
    IMAGE = "IMAGE"


class StoreTextAlignment(StrEnum):
    """StoreTextAlignment Description `LEFT` Left alignment. Default value configured for StoreEmptyTile `CENTER` Center alignment `RIGHT` Right alignment `JUSTIFY` Justified alignment"""

    CENTER = "CENTER"
    JUSTIFY = "JUSTIFY"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class StoreTextOption(StrEnum):
    """StoreTextOption Description `TEXT_OVER_IMAGE` Text overlaid on image `TEXT_NEXT_TO_IMAGE` Text next to image"""

    TEXT_NEXT_TO_IMAGE = "TEXT_NEXT_TO_IMAGE"
    TEXT_OVER_IMAGE = "TEXT_OVER_IMAGE"


class StoreTextOptionType(StrEnum):
    """StoreTextOptionType Description `NO_TEXT_OVER_VIDEO` No text overlay on video `TEXT_OVER_VIDEO` Text overlay on video"""

    NO_TEXT_OVER_VIDEO = "NO_TEXT_OVER_VIDEO"
    TEXT_OVER_VIDEO = "TEXT_OVER_VIDEO"


class StoreTileBorderSize(StrEnum):
    """StoreTileBorderSize Description `NONE` No border `SMALL` Small border size `MEDIUM` Medium border size `LARGE` Large border size"""

    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    NONE = "NONE"
    SMALL = "SMALL"


class StoreTileSize(StrEnum):
    """StoreTileSize Description `LARGE` Large tile size, StoreAWLSTile only uses LARGE `MEDIUM` Medium tile size `SMALL` Small tile size `MINI` Mini tile size"""

    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    MINI = "MINI"
    SMALL = "SMALL"


class StoreTileTextSize(StrEnum):
    """StoreTileTextSize Description `MINI` Mini text size `SMALL` Small text size `MEDIUM` Medium text size `LARGE` Large text size"""

    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    MINI = "MINI"
    SMALL = "SMALL"


class StoreTileType(StrEnum):
    """StoreTileType Description `TEXT` Tile type for StoreTextTile and tile layers `IMAGE` Tile type for StoreImageTile, StoreImageWithTextTile, StoreMetadataItem type `PRODUCT` Tile type for StoreProductTile and StoreShoppablePoint type `INTERACTIVE_IMAGE` Tile type for StoreShoppableImageTile `VIDEO` Tile type for StoreVideoTile `CUSTOM_CODE` Tile type for StoreCustomCodeTile `EMPTY` Tile type for StoreEmptyTile `EXTERNAL_WIDGET` Tile type for StoreAWLSTile"""

    CUSTOM_CODE = "CUSTOM_CODE"
    EMPTY = "EMPTY"
    EXTERNAL_WIDGET = "EXTERNAL_WIDGET"
    IMAGE = "IMAGE"
    INTERACTIVE_IMAGE = "INTERACTIVE_IMAGE"
    PRODUCT = "PRODUCT"
    TEXT = "TEXT"
    VIDEO = "VIDEO"


class StoreVerticalAlign(StrEnum):
    """StoreVerticalAlign Description `TOP` Top alignment `MIDDLE` Middle alignment `BOTTOM` Bottom alignment"""

    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    TOP = "TOP"


class StoreWidgetSectionType(StrEnum):
    """StoreWidgetSectionType Description `HERO` Section type for StoreHeroImageWidget `EDITORIAL_ROW` Widget type for StoreCustomCodeWidget, StoreImageWithTextWidget, StoreImageWidget, StoreProductWidget, StoreShoppableImageWidget, StoreTextWidget, StoreTileWidget, StoreVideoWidget and StoreAWLSWidget `DEALS_AND_COUPONS` Section type for StoreDealsWidget and StoreDealsContent type `GALLERY` Section type for StoreGalleryWidget `PRODUCT_COLLECTION` Section type for StoreProductCollectionWidget `PRODUCT_GRID` Section type for StoreProductGridWidget and type for StoreProductCollectionASINGrid `SHOP_THE_LOOK_CAROUSEL` Section type for StoreShopTheLookWidget and type for StoreShopTheLookContent `MANUALLY_CURATED_PRODUCT_CAROUSEL` Section type for StoreManuallyCuratedProductCarouselWidget and StoreCarouselContent type `RECOMMENDED` Section type for StoreProductCarouselWidget and StoreProductCarouselContent type `BEST_SELLING` Section type for StoreProductCarouselWidget and StoreProductCarouselContent type `PREMIUM_BEST_SELLING` Section type for StoreProductCarouselWidget and StoreProductCarouselContent type `LIVE_VIDEO` Section type for StoreLiveVideoWidget `BANNER` Section type for StoreBannerWidget"""

    BANNER = "BANNER"
    BEST_SELLING = "BEST_SELLING"
    DEALS_AND_COUPONS = "DEALS_AND_COUPONS"
    EDITORIAL_ROW = "EDITORIAL_ROW"
    GALLERY = "GALLERY"
    HERO = "HERO"
    LIVE_VIDEO = "LIVE_VIDEO"
    MANUALLY_CURATED_PRODUCT_CAROUSEL = "MANUALLY_CURATED_PRODUCT_CAROUSEL"
    PREMIUM_BEST_SELLING = "PREMIUM_BEST_SELLING"
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    PRODUCT_GRID = "PRODUCT_GRID"
    RECOMMENDED = "RECOMMENDED"
    SHOP_THE_LOOK_CAROUSEL = "SHOP_THE_LOOK_CAROUSEL"


class StoreWidgetType(StrEnum):
    """StoreWidgetType Description `HERO` Widget type for StoreHeroImageWidget `EDITORIAL_ROW` Widget type for StoreCustomCodeWidget, StoreImageWithTextWidget, StoreImageWidget, StoreProductWidget, StoreShoppableImageWidget, StoreTextWidget, StoreTileWidget, StoreVideoWidget and StoreAWLSWidget `PRODUCT_GRID` Widget type for StoreProductGridWidget and StoreDealsWidget `GALLERY` Widget type for StoreGalleryWidget and StoreGalleryContent type `PRODUCT_COLLECTION` Widget type for StoreProductCollectionWidget and StoreProductCollection type `MULTI_MEDIA_CAROUSEL` Widget type for StoreShopTheLookWidget, StoreManuallyCuratedProductCarouselWidget and StoreProductCarouselWidget `PRODUCT_CAROUSEL` Widget type for StoreProductCarouselWidget `LIVE_VIDEO` Widget type and content type for StoreLiveVideoWidget `BANNER` Widget type and content type for StoreBannerWidget"""

    BANNER = "BANNER"
    EDITORIAL_ROW = "EDITORIAL_ROW"
    GALLERY = "GALLERY"
    HERO = "HERO"
    LIVE_VIDEO = "LIVE_VIDEO"
    MULTI_MEDIA_CAROUSEL = "MULTI_MEDIA_CAROUSEL"
    PRODUCT_CAROUSEL = "PRODUCT_CAROUSEL"
    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    PRODUCT_GRID = "PRODUCT_GRID"


class VerticalPosition(StrEnum):
    """VerticalPosition Description `TOP` Top position `MIDDLE` Middle position `BOTTOM` Bottom position"""

    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    TOP = "TOP"


class BrandStorePage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    content: StorePageContent
    editionId: str  # Reference to the store edition
    pageId: str  # Unique identifier for the store page
    pageType: Annotated[StorePageType | str, lenient_enum(StorePageType)]
    storeEditionPublishId: str | None = None  # Optional identifier for the published version of this page
    storeId: str  # Identifier of the associated store


class BrandStorePageBrandStoreEditionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStorePageBrandStoreEditionPublishVersionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStorePageBrandStoreIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStorePagePageIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStorePageSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStorePages: list[BrandStorePage] | None = None
    nextToken: str | None = None


class BrandedRecipeDirection(BaseModel):
    """Represents a single step in a recipe's directions"""

    model_config = ConfigDict(extra="forbid")

    body: str  # Detailed instruction text for the direction step
    title: str  # Title or heading for the direction step


class BrandedRecipeIngredient(BaseModel):
    """Represents an ingredient in a branded recipe"""

    model_config = ConfigDict(extra="forbid")

    asinOverrides: list[str] | None = None  # List of ASIN overrides for the ingredient
    brand: str  # Brand name associated with the ingredient
    displayText: str  # Formatted text for displaying the ingredient
    isAsinRestricted: bool  # Flag indicating if ASIN is restricted for this ingredient
    isBrandRestricted: bool  # Flag indicating if brand is restricted for this ingredient
    isExclusiveOverride: bool  # Flag indicating if this ingredient has exclusive override
    name: str  # Name of the ingredient
    quantityList: list[BrandedRecipeQuantityItem] | None = None  # List of quantity measurements for the ingredient


class BrandedRecipeIngredientsMetadata(BaseModel):
    """Contains metadata information for recipe ingredients"""

    model_config = ConfigDict(extra="forbid")

    priorityAsins: list[PriorityAsin] | None = (
        None  # List of priority ASINs for ingredients with detailed product information
    )
    quantity: float | None = None  # Quantity amount for the ingredient
    searchText: str | None = None  # Search text for ingredient metadata
    translatedUnit: str | None = None  # Translated unit of measurement


class BrandedRecipeMedia(BaseModel):
    """Represents media content associated with a recipe"""

    model_config = ConfigDict(extra="forbid")

    altText: str | None = None  # Alternative text description of the media content
    assetLibraryId: str | None = None  # Identifier for the asset.
    mediaUrl: str | None = None  # URL of the media content


class BrandedRecipeQuantityItem(BaseModel):
    """Represents a quantity measurement for a recipe ingredient"""

    model_config = ConfigDict(extra="forbid")

    amount: float  # Numerical amount of the ingredient
    unit: str  # Unit of measurement for the ingredient


class BrandedRecipeWidget(BaseModel):
    """Main widget structure for displaying a branded recipe"""

    model_config = ConfigDict(extra="forbid")

    availableProductAsins: list[str] | None = None  # List of available product ASINs.
    desktopMedia: BrandedRecipeMedia | None = None
    directions: list[BrandedRecipeDirection] | None = None  # List of preparation directions for the recipe
    encodedIngredientComposition: str | None = None  # Encoded string containing ingredient composition details
    ingredientMetadata: list[BrandedRecipeIngredientsMetadata] | None = (
        None  # Metadata associated with recipe ingredients
    )
    ingredients: list[BrandedRecipeIngredient] | None = None  # List of ingredients required for the recipe
    isInitialLoad: bool | None = None  # Flag indicating if recipe is set to initial load
    mobileMedia: BrandedRecipeMedia | None = None
    preparationTime: str  # Time required to prepare the recipe
    refTag: str | None = None  # REF tracking tag for the branded recipe
    servingSize: float  # Number of servings the recipe yields
    title: str | None = None  # Title of the recipe


class CTI(BaseModel):
    model_config = ConfigDict(extra="forbid")

    category: str | None = None  # Category identifier.
    item: str | None = None  # Item identifier.
    type: str | None = None  # Type identifier.


class CommonTileProperties(BaseModel):
    model_config = ConfigDict(extra="forbid")

    size: Annotated[StoreTileSize | str, lenient_enum(StoreTileSize)]
    tag: str  # The unique tag for the tile to help track on performance.
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)]


class CommonWidgetProperties(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sectionType: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]
    widgetTag: str  # The unique tag for the widget to help track on performance.
    widgetType: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)]


class Coordinates(BaseModel):
    model_config = ConfigDict(extra="forbid")

    x: float | None = None  # X coordinate.
    y: float | None = None  # Y coordinate.


class PriorityAsin(BaseModel):
    """Product information for a priority ASIN"""

    model_config = ConfigDict(extra="forbid")

    addToCartActionParams: str  # Parameters for add to cart action
    bottleDepositFee: str | None = None  # Bottle deposit fee amount
    bottleDepositFeeString: str | None = None  # Bottle deposit fee as string
    cartQuantity: float  # Quantity of this item in the cart
    catalogDisplayPricePerUnitOfMeasure: str | None = None  # Price per unit of measure for display
    freshButton: str | None = None  # Fresh button information
    isAlternateSearchResult: bool  # Flag indicating if this is an alternate search result
    isRequiredQuantityInCart: bool  # Flag indicating if a quantity is required in cart
    isSoldByCount: bool  # Flag indicating if the product is sold by count
    itemAvailability: str  # Status of item availability
    offerId: str  # Unique identifier for the offer
    offerName: str  # Display name of the product offer
    offerUnit: str  # Unit of the offer (e.g., Fl Oz, lb)
    productAsin: str  # ASIN associated with this product
    productDetailsUrl: str  # URL to the product details page
    productImageUrl: str  # URL of the product image
    promotionDisplay: str | None = None  # Display text for active promotion
    promotionId: str | None = None  # Identifier for active promotion
    quantityInStock: float | None = None  # Available quantity in stock
    requiredQuantity: float  # Required quantity for purchase
    retailATCButton: str | None = None  # Retail add-to-cart button information
    reviewStars: ReviewStars | None = None
    searchTerm: str | None = None  # Search term associated with this product
    subtotalParams: str  # Subtotal parameters for pricing calculations
    vuomDisplayPrice: str  # Display price for virtual unit of measure


class QueryBrandStorePageRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionIdFilter: BrandStorePageBrandStoreEditionIdFilter
    maxResults: int | None = None
    nextToken: str | None = None
    pageIdFilter: BrandStorePagePageIdFilter
    storeEditionPublishIdFilter: BrandStorePageBrandStoreEditionPublishVersionIdFilter | None = None
    storeIdFilter: BrandStorePageBrandStoreIdFilter


class ReviewStars(BaseModel):
    """Review information for a product"""

    model_config = ConfigDict(extra="forbid")

    hasHalfStar: bool  # Flag indicating if the product has a half star in the rating
    reviewCount: int  # Number of reviews for the product
    wholeStars: int  # Number of whole stars in the rating


class StoreASINSlide(BaseModel):
    model_config = ConfigDict(extra="forbid")

    productAsin: str  # The ASIN of the product.
    tag: str  # Unique tag for the slide which will be ASIN.
    type: Annotated[StoreSlideType | str, lenient_enum(StoreSlideType)]


class StoreAWLSTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreAWLSTileContent | None = None
    externalWidgetId: str  # External widget identifier.


class StoreAWLSTileContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandedRecipeWidget: BrandedRecipeWidget | None = None
    storeProductSelectorWidget: StoreProductSelectorWidget | None = None
    storeVideoRevealWidget: StoreVideoRevealWidget | None = None


class StoreAWLSWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreAWLSTile]  # The AWLS tile configuration. Exactly one tile is required.
    widgetDependencies: list[str] | None = None  # List of widget dependencies.


class StoreBannerContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    banners: StoreBanners | None = None
    tag: str | None = None  # Unique tag for the content.
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)] | None = None


class StoreBannerWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreBannerContent


class StoreBanners(BaseModel):
    model_config = ConfigDict(extra="forbid")

    blackLivesMatter: bool  # Flag to display Black Lives Matter banner
    stopAsianHate: bool  # Flag to display Stop Asian Hate banner


class StoreCallToActionData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    customUrl: str | None = None  # Custom URL for the call to action.
    pageId: str | None = None  # Page identifier.
    productAsin: str | None = None  # ASIN for the call to action.
    text: str | None = None  # Call to action text.


class StoreCallToActionProductData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    customUrl: str | None = None  # Custom URL for the call to action.
    productAsin: str | None = None  # Product ASIN for the call to action.
    text: str | None = None  # Call to action text.


class StoreCanvasData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    canvasHeight: float | None = None  # Height in the canvas.
    height: float | None = None  # Height in the canvas.
    left: float | None = None  # Left position in the canvas.
    naturalHeight: float | None = None  # Natural height of the image.
    naturalWidth: float | None = None  # Natural width of the image.
    top: float | None = None  # Top position in the canvas.
    width: float | None = None  # Width in the canvas.


class StoreCarouselContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bulk: bool  # Whether this is a bulk configuration.
    callToActionData: StoreCallToActionData
    includeOutOfStock: bool  # Whether to include out of stock items.
    keyword: str  # Keyword for product filtering.
    productAsins: list[str] | None = None  # List of ASINs, maximum 500 unique items.
    search: StoreCarouselSearch | None = None
    slides: list[StoreASINSlide] | None = None  # List of ASIN slides.
    tag: str  # Unique tag for the content to track performance.
    text: str  # Description text.
    title: str  # Title of the carousel.
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]


class StoreCarouselSearch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    includeOutOfStock: bool  # Whether to include out of stock items in search.
    keyword: str  # Search keyword.
    node: str  # Node identifier for search.
    productAsins: list[str] | None = None  # List of ASINs for search filtering.


class StoreCropBoxData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    height: float | None = None  # Height of the crop box.
    left: float | None = None  # Left position of the crop box.
    top: float | None = None  # Top position of the crop box.
    width: float | None = None  # Width of the crop box.


class StoreCroppedImage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    altText: str | None = None  # Alternative text for the image.
    assetId: str | None = None  # Asset identifier.
    canvasData: StoreCanvasData | None = None
    cropBox: StoreCropBoxData | None = None
    imageKey: str | None = None  # Key identifier for the image.
    imageNaturalHeight: float | None = None  # Natural height of the image.
    imageNaturalWidth: float | None = None  # Natural width of the image.
    imageUrl: str | None = None  # URL of the image.


class StoreCustomCodeContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    autoDimension: bool | None = None  # Whether to use automatic dimensioning.
    availableProductAsins: list[str] | None = None  # List of available ASINs, maximum 500 unique items.
    cti: CTI | None = None
    embedCode: str | None = None  # Embedded code content.
    integrity: str | None = None  # Integrity hash for security.
    widgetName: str | None = None  # Name of the widget.
    widgetTag: str | None = None  # Widget identifier.


class StoreCustomCodeTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreCustomCodeContent | None = None


class StoreCustomCodeWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreCustomCodeTile]  # The custom code tile configuration. Exactly one tile is required.


class StoreDealsConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    node: str | None = None  # Node identifier for deals.


class StoreDealsContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    deals: StoreDealsConfig | None = None
    dealsMode: Annotated[StoreDealsMode | str, lenient_enum(StoreDealsMode)] | None = None
    productAsins: list[str] | None = None  # List of ASINs, maximum 500 unique items.
    tag: str | None = None  # Unique tag for the content to track performance.
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)] | None = None


class StoreDealsWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreDealsContent | None = None


class StoreEmptyTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreEmptyTileContent


class StoreEmptyTileContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bondCustomerServiceLink: bool | None = None  # Whether to include a customer service link.
    callToAction: str | None = None  # Call to action text.
    text: str | None = None  # Text content (must be empty).
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = None
    title: str | None = None  # Title of the tile (must be empty).


class StoreGalleryContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    metadata: list[StoreMetadataItem] | None = None  # Metadata associated with the gallery.
    slides: list[StoreGallerySlide] | None = None  # List of slides in the gallery.
    tag: str | None = None  # Unique tag for the content.
    text: str | None = None  # Text content of the gallery.
    title: str | None = None  # Title of the gallery.
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)] | None = None


class StoreGallerySlide(BaseModel):
    model_config = ConfigDict(extra="forbid")

    alt: str | None = None  # Alternative text for the slide.
    assetId: str | None = None  # Asset identifier for the slide.
    imageKey: str | None = None  # Key identifier for the image.
    type: Annotated[StoreSlideType | str, lenient_enum(StoreSlideType)] | None = None


class StoreGalleryWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreGalleryContent | None = None


class StoreHeroContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str | None = None  # Identifier for the asset.
    assetTags: str | None = None  # Tags associated with the asset.
    canvasData: StoreCanvasData | None = None
    description: str | None = None  # Description of the hero image.
    imageHeight: float | None = None  # Height of the hero image.
    imageKey: str | None = None  # Key identifier for the image.
    imageOffsetLeft: float | None = None  # Left offset of the image.
    imageOffsetTop: float | None = None  # Top offset of the image.
    imageUrl: str  # URL of the hero image.
    imageWidth: float | None = None  # Width of the hero image.
    mobileContent: StoreMobileContent | None = None
    tag: str | None = None  # Unique tag for the content.
    textOverlay: str | None = None  # Text overlay displayed on the hero image.


class StoreHeroImageWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreHeroContent | None = None


class StoreImageContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    altText: str | None = None  # Alternative text for the image.
    assetId: str | None = None  # Asset identifier.
    assetTags: str | None = None  # Tags associated with the asset.
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = None
    callToAction: str | None = None  # Call to action text.
    canvasData: StoreCanvasData | None = None
    cropBoxData: StoreCropBoxData | None = None
    customUrl: str | None = None  # Custom URL.
    hideTitle: bool | None = None  # Whether to hide the title.
    imageHeight: float | None = None  # Height of the image.
    imageKey: str | None = None  # Key identifier for the image.
    imageOffsetLeft: float | None = None  # Left offset for image positioning.
    imageOffsetTop: float | None = None  # Top offset for image positioning.
    imageUrl: str | None = None  # URL of the image.
    imageWidth: float | None = None  # Width of the image.
    isAiGen: bool | None = None  # Whether the image is AI-generated.
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = None
    pageId: str | None = None  # Page identifier.
    productAsins: list[str] | None = None  # Single ASIN for the image.
    text: str | None = None  # Text content.
    textAlign: Annotated[StoreImageTextAlign | str, lenient_enum(StoreImageTextAlign)] | None = None
    tileLayers: list[str] | None = None  # Layer configuration for the tile.
    title: str | None = None  # Title of the image.
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = None


class StoreImageSlide(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str | None = None  # Asset identifier.
    assetTags: str | None = None  # Tags associated with the asset.
    canvasData: StoreCanvasData | None = None
    imageHeight: float | None = None  # Height of the image.
    imageKey: str | None = None  # Key identifier for the image.
    imageOffsetLeft: float | None = None  # Left offset for image positioning.
    imageOffsetTop: float | None = None  # Top offset for image positioning.
    imageUrl: str | None = None  # URL of the image.
    imageWidth: float | None = None  # Width of the image.
    tag: str | None = None  # Unique identifier for the slide.
    type: Annotated[StoreSlideType | str, lenient_enum(StoreSlideType)] | None = None


class StoreImageTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreImageContent | None = None
    flexHeight: bool | None = None  # Whether the height is flexible.
    mobileContent: StoreMobileImageContent | None = None
    uploadMobileImage: bool | None = None  # Whether to upload a mobile-specific image.


class StoreImageWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreImageTile]  # The image tile configuration. Exactly one tile is required.


class StoreImageWithTextContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    altText: str | None = None  # Alternative text for the image.
    assetId: str | None = None  # Asset identifier.
    assetTags: str | None = None  # Tags associated with the asset.
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = None
    callToAction: str | None = None  # Call to action text.
    canvasData: StoreCanvasData | None = None
    cropBoxData: StoreCropBoxData | None = None
    customUrl: str | None = None  # Custom URL.
    hideTitle: bool | None = None  # Whether to hide the title.
    imageHeight: float | None = None  # Height of the image.
    imageKey: str | None = None  # Key identifier for the image.
    imageOffsetLeft: float | None = None  # Left offset for image positioning.
    imageOffsetTop: float | None = None  # Top offset for image positioning.
    imageUrl: str | None = None  # URL of the image.
    imageWidth: float | None = None  # Width of the image.
    isAiGen: bool | None = None  # Whether the image is AI-generated.
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = None
    pageId: str | None = None  # Page identifier.
    productAsins: list[str] | None = None  # Single ASIN for the image.
    renderTileLayers: bool | None = None  # Whether to render tile layers.
    shape: Annotated[StoreImageShape | str, lenient_enum(StoreImageShape)] | None = None
    text: str | None = None  # Text content.
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = None
    textOption: Annotated[StoreTextOption | str, lenient_enum(StoreTextOption)] | None = None
    tileLayers: list[StoreTileLayer] | None = None  # Layer configuration for the tile.
    title: str | None = None  # Title of the image.
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = None


class StoreImageWithTextTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreImageWithTextContent | None = None
    flexHeight: bool | None = None  # Whether the height is flexible.
    mobileContent: StoreMobileImageWithTextContent | None = None
    uploadMobileImage: bool | None = None  # Whether to upload a mobile-specific image.
    variation: Annotated[StoreImageWithTextTileVariation | str, lenient_enum(StoreImageWithTextTileVariation)]


class StoreImageWithTextWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreImageWithTextTile]  # The image with text tile configuration. Exactly one tile is required.


class StoreLiveVideoContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    channel: str | None = None  # Channel of the video.
    tag: str  # Unique tag for the content.
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)]


class StoreLiveVideoWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreLiveVideoContent


class StoreManuallyCuratedProductCarouselWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreCarouselContent | None = None


class StoreMetadataItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    alt: str | None = None  # Alternative text.
    assetId: str | None = None  # Asset identifier.
    filename: str | None = None  # Name of the file.
    imageKey: str | None = None  # Key identifier for the image.
    imageUrl: str | None = None  # The imageUrl of the item.
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)] | None = None
    url: str | None = None  # URL of the item.


class StoreMobileContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str | None = None  # Asset identifier for mobile view.
    assetTags: str | None = None  # Asset tags for mobile view.
    canvasData: StoreCanvasData | None = None
    imageHeight: float | None = None  # Height of the image for mobile view.
    imageKey: str | None = None  # Image key for mobile view.
    imageOffsetLeft: float | None = None  # Left offset of the image for mobile view.
    imageOffsetTop: float | None = None  # Top offset of the image for mobile view.
    imageUrl: str | None = None  # URL of the image for mobile view.
    imageWidth: float | None = None  # Width of the image for mobile view.
    version: str | None = None  # Version identifier for mobile content


class StoreMobileImageContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    altText: str | None = None  # Alternative text for the mobile image.
    assetId: str | None = None  # Asset identifier for mobile.
    assetTags: str | None = None  # Tags associated with the mobile asset.
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = None
    canvasData: StoreCanvasData | None = None
    cropBoxData: StoreCropBoxData | None = None
    hideTitle: bool | None = None  # Whether to hide the title on mobile.
    imageHeight: float | None = None  # Height of the mobile image.
    imageKey: str | None = None  # Key identifier for the mobile image.
    imageOffsetLeft: float | None = None  # Left offset for mobile image positioning.
    imageOffsetTop: float | None = None  # Top offset for mobile image positioning.
    imageUrl: str | None = None  # URL of the mobile image.
    imageWidth: float | None = None  # Width of the mobile image.
    isAiGen: bool | None = None  # Whether the mobile image is AI-generated.
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = None
    tileLayers: list[str] | None = None  # Layer configuration for the mobile tile.
    title: str | None = None  # Title for mobile display.
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = None


class StoreMobileImageWithTextContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    altText: str | None = None  # Alternative text for the mobile image.
    assetId: str | None = None  # Asset identifier for mobile.
    assetTags: str | None = None  # Tags associated with the mobile asset.
    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = None
    canvasData: StoreCanvasData | None = None
    cropBoxData: StoreCropBoxData | None = None
    hideTitle: bool | None = None  # Whether to hide the title on mobile.
    imageHeight: float | None = None  # Height of the mobile image.
    imageKey: str | None = None  # Key identifier for the mobile image.
    imageOffsetLeft: float | None = None  # Left offset for mobile image positioning.
    imageOffsetTop: float | None = None  # Top offset for mobile image positioning.
    imageUrl: str | None = None  # URL of the mobile image.
    imageWidth: float | None = None  # Width of the mobile image.
    isAiGen: bool | None = None  # Whether the mobile image is AI-generated.
    layout: Annotated[StoreImageLayout | str, lenient_enum(StoreImageLayout)] | None = None
    renderTileLayers: bool | None = None  # Whether to render tile layers on mobile.
    shape: Annotated[StoreImageShape | str, lenient_enum(StoreImageShape)] | None = None
    text: str | None = None  # Text content for mobile.
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = None
    textOption: Annotated[StoreTextOption | str, lenient_enum(StoreTextOption)] | None = None
    tileLayers: list[StoreTileLayer] | None = None  # Layer configuration for the mobile tile.
    title: str | None = None  # Title for mobile display.
    verticalAlign: Annotated[StoreVerticalAlign | str, lenient_enum(StoreVerticalAlign)] | None = None


class StorePageContent(BaseModel):
    """Structure containing the content elements of a store page"""

    model_config = ConfigDict(extra="forbid")

    description: str | None = None  # Description of the page
    template: Annotated[StorePageTemplate | str, lenient_enum(StorePageTemplate)]
    title: str | None = None  # For store page, title of the page; for SB landing page, this can be optional
    widgets: list[StorePageWidget] | None = None  # Collection of widgets displayed on the page


class StorePageWidget(BaseModel):
    """Union of all possible widget types that can be used on a store page"""

    model_config = ConfigDict(extra="forbid")

    storeHeroImageWidget: StoreHeroImageWidget | None = None
    storeTileWidget: StoreTileWidget | None = None
    storeImageWidget: StoreImageWidget | None = None
    storeTextWidget: StoreTextWidget | None = None
    storeImageWithTextWidget: StoreImageWithTextWidget | None = None
    storeProductCollectionWidget: StoreProductCollectionWidget | None = None
    storeProductGridWidget: StoreProductGridWidget | None = None
    storeDealsWidget: StoreDealsWidget | None = None
    storeProductWidget: StoreProductWidget | None = None
    storeShoppableImageWidget: StoreShoppableImageWidget | None = None
    storeCustomCodeWidget: StoreCustomCodeWidget | None = None
    storeVideoWidget: StoreVideoWidget | None = None
    storeGalleryWidget: StoreGalleryWidget | None = None
    storeShopTheLookWidget: StoreShopTheLookWidget | None = None
    storeManuallyCuratedProductCarouselWidget: StoreManuallyCuratedProductCarouselWidget | None = None
    storeAWLSWidget: StoreAWLSWidget | None = None
    storeBannerWidget: StoreBannerWidget | None = None
    storeProductCarouselWidget: StoreProductCarouselWidget | None = None
    storeLiveVideoWidget: StoreLiveVideoWidget | None = None


class StoreProductCarouselContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    callToActionData: StoreCallToActionProductData | None = None
    searchContent: StoreProductCarouselSearch | None = None
    tag: str  # Unique tag for the content.
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]


class StoreProductCarouselSearch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    node: str | None = None  # Node identifier for search
    type: Annotated[StoreProductCarouselSearchType | str, lenient_enum(StoreProductCarouselSearchType)] | None = None


class StoreProductCarouselWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreProductCarouselContent


class StoreProductCollectionASINGrid(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bulk: bool | None = None  # Whether this is a bulk configuration.
    description: str | None = None  # Description of the product grid.
    displayProductGridHeader: bool | None = None  # Whether to display the product grid header.
    includeOutOfStock: bool | None = None  # Whether to include out of stock products.
    isAutomatedProductGrid: bool | None = None  # Whether the product grid is automatically populated
    keyword: str | None = None  # Keyword for product filtering.
    productAsins: list[str] | None = None  # List of ASINs, maximum 60 unique items.
    sort: str | None = None  # Sort order for products.
    tag: str | None = None  # Unique tag for the tile to track performance.
    title: str | None = None  # Title of the product grid.
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)]
    variation: str | None = None  # Variation of the product grid.


class StoreProductCollectionContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    collectionTags: str | None = None  # Tags associated with the collection.
    productGridConversionTimestamp: float | None = None  # Timestamp of product grid conversion.
    tag: str | None = None  # Unique tag for the content.
    type: Annotated[StoreWidgetType | str, lenient_enum(StoreWidgetType)] | None = None


class StoreProductCollectionImageTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreImageWithTextContent | None = None
    flexHeight: bool | None = None  # Whether the height is flexible.
    mobileContent: StoreMobileImageWithTextContent | None = None
    uploadMobileImage: bool | None = None  # Whether to upload a mobile-specific image.
    variation: Annotated[StoreImageWithTextTileVariation | str, lenient_enum(StoreImageWithTextTileVariation)]


class StoreProductCollectionTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    storeProductCollectionImageTile: StoreProductCollectionImageTile | None = None
    storeProductCollectionASINGrid: StoreProductCollectionASINGrid | None = None


class StoreProductCollectionWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    aiMetadata: list[Tag] | None = None  # Metadata about AI generated fields.
    commonProperties: CommonWidgetProperties
    content: StoreProductCollectionContent | None = None
    tiles: list[StoreProductCollectionTile]  # The tiles for the product collection. Exactly two tiles are required.


class StoreProductGridContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bulk: bool | None = None  # Whether this is a bulk product grid.
    description: str | None = None  # Description of the product grid.
    displayProductGridHeader: bool | None = None  # Whether to display the grid header.
    excludedProductAsins: list[str] | None = None  # List of product ASINs exclude when dynamic.
    includeOutOfStock: bool | None = None  # Whether to include out of stock products.
    isAutomatedProductGrid: bool | None = None  # Whether the product grid is automatically populated
    keyword: str | None = None  # Keyword for product filtering.
    pinnedProductAsins: list[str] | None = None  # List of product ASINs include when dynamic.
    productAsins: list[str] | None = None  # List of product ASINs.
    productType: str | None = None  # Type of products to display
    search: StoreProductGridSearch | None = None
    showOnlyMarkdown: bool | None = None  # Whether to only show products on markdown.
    sort: str | None = None  # Sort order for products.
    tag: str | None = None  # Unique tag for the content.
    title: str | None = None  # Title of the product grid.
    type: str | None = None  # Type of the content.


class StoreProductGridSearch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandId: str | None = None  # brand id to search.
    includeOutOfStock: bool | None = None  # Whether to include out of stock products in search.
    keyword: str | None = None  # Search keyword.
    node: str | None = None  # Node identifier for search.
    productAsins: list[str] | None = None  # List of product ASINs.
    sort: str | None = None  # Sort order for search results.


class StoreProductGridWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreProductGridContent


class StoreProductSelectorAnswer(BaseModel):
    """Represents a possible answer in the product selector questionnaire"""

    model_config = ConfigDict(extra="forbid")

    image: StoreProductSelectorImage | None = None
    nextStep: str  # Reference to the next question or step in the selection flow
    productAsins: list[str] | None = None  # List of ASINs associated with this answer
    tag: str  # Unique identifier for the answer
    text: str | None = None  # Display text for the answer option


class StoreProductSelectorDesignOptions(BaseModel):
    """Visual styling options for the product selector widget"""

    model_config = ConfigDict(extra="forbid")

    backgroundColor: str  # Background color in hex or named color value
    backgroundShape: str  # Shape of the background container
    buttonColor: (
        Annotated[StoreProductSelectorButtonColor | str, lenient_enum(StoreProductSelectorButtonColor)] | None
    ) = None
    buttonShape: str  # Shape style for buttons in the selector
    textAlignment: str  # Alignment of text elements (left, center, right)
    textSize: str  # Size of the text elements
    textStyle: str  # Font family or style to be used
    textWeight: str  # Font weight for text elements


class StoreProductSelectorImage(BaseModel):
    """Represents an image used in the product selector introduction"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # Asset ID of the image
    fileName: str | None = None  # File name of the image
    imageUrl: str  # URL of the image
    layout: Annotated[StoreProductSelectorImageLayout | str, lenient_enum(StoreProductSelectorImageLayout)] | None = (
        None
    )


class StoreProductSelectorImageOptions(BaseModel):
    """Image options for the product selector introduction"""

    model_config = ConfigDict(extra="forbid")

    image: StoreProductSelectorImage
    layoutConfiguration: StoreProductSelectorLayoutConfiguration


class StoreProductSelectorIntroduction(BaseModel):
    """Introduction section for the product selector widget"""

    model_config = ConfigDict(extra="forbid")

    buttonText: str  # Text displayed on the introduction button
    description: str  # Description text for the introduction section
    heading: str  # Heading text for the introduction section
    headline: str | None = None  # Headline text for the introduction section
    imageOptions: StoreProductSelectorImageOptions
    isEnabled: bool  # Flag indicating whether the introduction is enabled


class StoreProductSelectorLayoutConfiguration(BaseModel):
    """Layout configuration for desktop and mobile views"""

    model_config = ConfigDict(extra="forbid")

    desktopLayout: Annotated[StoreProductSelectorImageLayout | str, lenient_enum(StoreProductSelectorImageLayout)]
    mobileLayout: Annotated[StoreProductSelectorImageLayout | str, lenient_enum(StoreProductSelectorImageLayout)]


class StoreProductSelectorQuestion(BaseModel):
    """Represents a question in the product selector questionnaire"""

    model_config = ConfigDict(extra="forbid")

    answerList: list[StoreProductSelectorAnswer] | None = None  # List of possible answers for this question
    areImagesEnabled: bool | None = None  # Flag indicating whether images are enabled
    description: str | None = None  # Additional descriptive text or context for the question
    hasImage: bool | None = None  # Flag indicating whether the question has an image
    tag: str  # Unique identifier for the question
    text: str | None = None  # Main question text displayed to the user


class StoreProductSelectorResults(BaseModel):
    """Configuration for displaying product selector results"""

    model_config = ConfigDict(extra="forbid")

    buttonText: str | None = None  # Text to display on the call-to-action button
    description: str | None = None  # Descriptive text explaining the results
    disclaimer: str  # Legal or additional information text for the results
    headline: str  # Main heading text for the results section
    storeUrl: str | None = None  # URL to the store page for the selected products


class StoreProductSelectorWidget(BaseModel):
    """Main widget structure for the product selector feature"""

    model_config = ConfigDict(extra="forbid")

    designOptions: StoreProductSelectorDesignOptions
    introduction: StoreProductSelectorIntroduction | None = None
    productAsins: list[str] | None = None  # Master list of ASINs available in the selector
    questionList: list[StoreProductSelectorQuestion] | None = None  # Ordered list of questions in the selector flow
    results: StoreProductSelectorResults


class StoreProductTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreProductTileContent | None = None


class StoreProductTileContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bleedImage: Annotated[StoreBleedImageType | str, lenient_enum(StoreBleedImageType)] | None = None
    displayOutOfStockASIN: bool | None = None  # Whether to display out of stock ASIN.
    layout: Annotated[StoreLayoutType | str, lenient_enum(StoreLayoutType)] | None = None
    productAsins: list[str] | None = None  # Single ASIN for the product.
    text: str | None = None  # Description text for the product.
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = None
    title: str | None = None  # Title of the product.


class StoreProductWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreProductTile]  # The product tile configuration. Exactly one tile is required.


class StoreShopTheLookContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bulk: bool | None = None  # Whether this is a bulk configuration.
    callToActionData: StoreCallToActionData | None = None
    includeOutOfStock: bool | None = None  # Whether to include out of stock items.
    keyword: str | None = None  # Keyword for searching.
    productAsins: list[str] | None = None  # List of product ASINs, maximum 25 unique items.
    search: StoreShopTheLookSearch | None = None
    slides: list[StoreShopTheLookSlide] | None = None  # List of slides in the carousel.
    tag: str | None = None  # Unique tag for the content.
    text: str | None = None  # Text content.
    title: str | None = None  # Title of the content.
    type: Annotated[StoreWidgetSectionType | str, lenient_enum(StoreWidgetSectionType)] | None = None


class StoreShopTheLookSearch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    includeOutOfStock: bool | None = None  # Whether to include out of stock items in search.
    keyword: str | None = None  # Search keyword.
    node: str | None = None  # Node identifier for search.
    productAsins: list[str] | None = None  # Single ASIN for search filtering.


class StoreShopTheLookSlide(BaseModel):
    model_config = ConfigDict(extra="forbid")

    storeImageSlide: StoreImageSlide | None = None
    storeASINSlide: StoreASINSlide | None = None


class StoreShopTheLookWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    content: StoreShopTheLookContent | None = None


class StoreShoppableImageContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    croppedImage: StoreCroppedImage | None = None
    points: list[StoreShoppablePoint] | None = None  # Interactive points on the image.
    productAsins: list[str] | None = None  # Single ASIN for the point.
    renderTileLayers: bool | None = None  # Whether to render tile layers.
    textOption: Annotated[StoreShoppableTextOption | str, lenient_enum(StoreShoppableTextOption)] | None = None
    tileLayers: list[StoreTileLayer] | None = None  # Layer configuration for the tile.


class StoreShoppableImageTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreShoppableImageContent | None = None


class StoreShoppableImageWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreShoppableImageTile]  # The shoppable image tile configuration. Exactly one tile is required.


class StoreShoppablePoint(BaseModel):
    model_config = ConfigDict(extra="forbid")

    coordinates: Coordinates
    productAsins: list[str] | None = None  # Single ASIN for the point.
    tag: str | None = None  # Unique tag for the point.
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)] | None = None


class StoreTextContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bold: bool  # Whether text should be bold.
    bondCustomerServiceLink: bool | None = None  # Whether to include customer service link.
    callToAction: str | None = None  # Call to action text.
    customUrl: str | None = None  # Custom URL for the content.
    pageId: str | None = None  # Identifier for the page.
    productAsins: list[str] | None = None  # Single product ASIN for the content.
    text: str  # Main text content.
    textAlign: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = None
    title: str  # Title of the content.
    uppercase: bool  # Whether text should be uppercase.


class StoreTextTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreTextContent | None = None


class StoreTextWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreTextTile]  # Single text tile configuration.


class StoreTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    storeImageWithTextTile: StoreImageWithTextTile | None = None
    storeImageTile: StoreImageTile | None = None
    storeProductTile: StoreProductTile | None = None
    storeShoppableImageTile: StoreShoppableImageTile | None = None
    storeTextTile: StoreTextTile | None = None
    storeVideoTile: StoreVideoTile | None = None
    storeEmptyTile: StoreEmptyTile | None = None
    storeCustomCodeTile: StoreCustomCodeTile | None = None


class StoreTileLayer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    colorPalette: Annotated[StoreColorPalette | str, lenient_enum(StoreColorPalette)] | None = None
    content: StoreTileLayerContent | None = None
    coverTile: bool | None = None  # Whether the layer covers the entire tile.
    margin: Annotated[StoreTileBorderSize | str, lenient_enum(StoreTileBorderSize)] | None = None
    opacity: float | None = None  # Opacity level of the layer.
    outOfBounds: bool | None = None  # Whether the layer is out of bounds.
    padding: Annotated[StoreTileBorderSize | str, lenient_enum(StoreTileBorderSize)] | None = None
    position: StoreTilePosition | None = None
    tag: str | None = None  # Unique tag for the tile layer to track performance.
    type: Annotated[StoreTileType | str, lenient_enum(StoreTileType)] | None = None


class StoreTileLayerContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bodyText: str | None = None  # Body text for the layer.
    bondCustomerServiceLink: bool | None = None  # Whether to include a customer service link.
    callToAction: str | None = None  # Call to action text for the layer.
    callToActionType: Annotated[StoreCallToActionType | str, lenient_enum(StoreCallToActionType)] | None = None
    customUrl: str | None = None  # Custom URL for the layer.
    headerText: str | None = None  # Header text for the layer.
    pageId: str | None = None  # Page identifier for the layer.
    prefixText: str | None = None  # Prefix text for the layer.
    productAsins: list[str] | None = None  # Single ASIN for the layer.
    tileTextAlignment: Annotated[StoreTextAlignment | str, lenient_enum(StoreTextAlignment)] | None = None
    tileTextSize: Annotated[StoreTileTextSize | str, lenient_enum(StoreTileTextSize)] | None = None


class StoreTilePosition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    x: Annotated[HorizontalPosition | str, lenient_enum(HorizontalPosition)] | None = None
    y: Annotated[VerticalPosition | str, lenient_enum(VerticalPosition)] | None = None


class StoreTileWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    rowHeight: int | None = None  # Height of the row in pixels.
    tiles: list[StoreTile]  # The tiles for the widget. Minimum 2 and maximum 8 tiles are allowed.


class StoreVideoContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    assetId: str | None = None  # Asset identifier.
    assetTags: str | None = None  # Tags associated with the asset.
    autoPlay: bool | None = None  # Whether video should auto-play.
    callToAction: str | None = None  # Call to action text.
    canvasData: StoreCanvasData | None = None
    customUrl: str | None = None  # Custom URL for the content.
    imageHeight: float | None = None  # Height of the image.
    imageKey: str | None = None  # Key for the image asset.
    imageOffsetLeft: float | None = None  # Left offset for image positioning.
    imageOffsetTop: float | None = None  # Top offset for image positioning.
    imageUrl: str | None = None  # URL of the image.
    imageWidth: float | None = None  # Width of the image.
    mute: bool | None = None  # Whether video should be muted.
    pageId: str | None = None  # Page identifier
    productAsins: list[str] | None = None  # List of product ASINs.
    renderTileLayers: bool | None = None  # Whether to render tile layers.
    resourceId: str | None = None  # Resource identifier.
    text: str | None = None  # Text content.
    textAlign: str | None = None  # Text alignment.
    textOption: Annotated[StoreTextOptionType | str, lenient_enum(StoreTextOptionType)] | None = None
    tileLayers: list[StoreTileLayer] | None = None  # Configuration for tile layers.
    title: str | None = None  # Title of the content.
    videoAssetId: str | None = None  # Video asset identifier.
    videoAssetTags: str | None = None  # Tags associated with the video asset.
    videoDescription: str | None = None  # Description of the video.
    videoKey: str | None = None  # Key for the video asset.
    videoName: str | None = None  # Name of the video.
    videoSize: float | None = None  # Size of the video in bytes.
    videoUrl: str | None = None  # URL of the video.


class StoreVideoRevealVRVideo(BaseModel):
    """Configuration for a single video reveal video asset"""

    model_config = ConfigDict(extra="forbid")

    assetId: str  # Unique identifier for the video asset
    url: str  # URL of the video content


class StoreVideoRevealVideos(BaseModel):
    """Collection of video assets for different device types"""

    model_config = ConfigDict(extra="forbid")

    desktop: StoreVideoRevealVRVideo
    mobile: StoreVideoRevealVRVideo


class StoreVideoRevealWidget(BaseModel):
    """Main widget structure for the video reveal feature"""

    model_config = ConfigDict(extra="forbid")

    backgroundColor: str  # Background color (CSS property)
    csmTag: str  # CSM tracking tag for the video reveal
    fadeoutDuration: str  # Fadeout duration (in ms)
    objectFit: str  # Object fit (CSS property)
    skipReveal: bool  # Skip reveal (to be used in development only)
    throttleLimit: str  # Play video every X minutes
    videos: StoreVideoRevealVideos


class StoreVideoTile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonTileProperties
    content: StoreVideoContent | None = None


class StoreVideoWidget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    commonProperties: CommonWidgetProperties
    tiles: list[StoreVideoTile]  # The content configuration for the video widget.


class Tag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.


__all__ = [
    "HorizontalPosition",
    "StoreBleedImageType",
    "StoreCallToActionType",
    "StoreColorPalette",
    "StoreDealsMode",
    "StoreImageLayout",
    "StoreImageShape",
    "StoreImageTextAlign",
    "StoreImageWithTextTileVariation",
    "StoreLayoutType",
    "StorePageTemplate",
    "StorePageType",
    "StoreProductCarouselSearchType",
    "StoreProductSelectorButtonColor",
    "StoreProductSelectorImageLayout",
    "StoreShoppableTextOption",
    "StoreSlideType",
    "StoreTextAlignment",
    "StoreTextOption",
    "StoreTextOptionType",
    "StoreTileBorderSize",
    "StoreTileSize",
    "StoreTileTextSize",
    "StoreTileType",
    "StoreVerticalAlign",
    "StoreWidgetSectionType",
    "StoreWidgetType",
    "VerticalPosition",
    "BrandStorePage",
    "BrandStorePageBrandStoreEditionIdFilter",
    "BrandStorePageBrandStoreEditionPublishVersionIdFilter",
    "BrandStorePageBrandStoreIdFilter",
    "BrandStorePagePageIdFilter",
    "BrandStorePageSuccessResponse",
    "BrandedRecipeDirection",
    "BrandedRecipeIngredient",
    "BrandedRecipeIngredientsMetadata",
    "BrandedRecipeMedia",
    "BrandedRecipeQuantityItem",
    "BrandedRecipeWidget",
    "CTI",
    "CommonTileProperties",
    "CommonWidgetProperties",
    "Coordinates",
    "PriorityAsin",
    "QueryBrandStorePageRequest",
    "ReviewStars",
    "StoreASINSlide",
    "StoreAWLSTile",
    "StoreAWLSTileContent",
    "StoreAWLSWidget",
    "StoreBannerContent",
    "StoreBannerWidget",
    "StoreBanners",
    "StoreCallToActionData",
    "StoreCallToActionProductData",
    "StoreCanvasData",
    "StoreCarouselContent",
    "StoreCarouselSearch",
    "StoreCropBoxData",
    "StoreCroppedImage",
    "StoreCustomCodeContent",
    "StoreCustomCodeTile",
    "StoreCustomCodeWidget",
    "StoreDealsConfig",
    "StoreDealsContent",
    "StoreDealsWidget",
    "StoreEmptyTile",
    "StoreEmptyTileContent",
    "StoreGalleryContent",
    "StoreGallerySlide",
    "StoreGalleryWidget",
    "StoreHeroContent",
    "StoreHeroImageWidget",
    "StoreImageContent",
    "StoreImageSlide",
    "StoreImageTile",
    "StoreImageWidget",
    "StoreImageWithTextContent",
    "StoreImageWithTextTile",
    "StoreImageWithTextWidget",
    "StoreLiveVideoContent",
    "StoreLiveVideoWidget",
    "StoreManuallyCuratedProductCarouselWidget",
    "StoreMetadataItem",
    "StoreMobileContent",
    "StoreMobileImageContent",
    "StoreMobileImageWithTextContent",
    "StorePageContent",
    "StorePageWidget",
    "StoreProductCarouselContent",
    "StoreProductCarouselSearch",
    "StoreProductCarouselWidget",
    "StoreProductCollectionASINGrid",
    "StoreProductCollectionContent",
    "StoreProductCollectionImageTile",
    "StoreProductCollectionTile",
    "StoreProductCollectionWidget",
    "StoreProductGridContent",
    "StoreProductGridSearch",
    "StoreProductGridWidget",
    "StoreProductSelectorAnswer",
    "StoreProductSelectorDesignOptions",
    "StoreProductSelectorImage",
    "StoreProductSelectorImageOptions",
    "StoreProductSelectorIntroduction",
    "StoreProductSelectorLayoutConfiguration",
    "StoreProductSelectorQuestion",
    "StoreProductSelectorResults",
    "StoreProductSelectorWidget",
    "StoreProductTile",
    "StoreProductTileContent",
    "StoreProductWidget",
    "StoreShopTheLookContent",
    "StoreShopTheLookSearch",
    "StoreShopTheLookSlide",
    "StoreShopTheLookWidget",
    "StoreShoppableImageContent",
    "StoreShoppableImageTile",
    "StoreShoppableImageWidget",
    "StoreShoppablePoint",
    "StoreTextContent",
    "StoreTextTile",
    "StoreTextWidget",
    "StoreTile",
    "StoreTileLayer",
    "StoreTileLayerContent",
    "StoreTilePosition",
    "StoreTileWidget",
    "StoreVideoContent",
    "StoreVideoRevealVRVideo",
    "StoreVideoRevealVideos",
    "StoreVideoRevealWidget",
    "StoreVideoTile",
    "StoreVideoWidget",
    "Tag",
]
